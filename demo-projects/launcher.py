"""
Demo Projects hub — RubberDuck-styled control plane.

Serves the dashboard HTML and launches/stops demos with live logs.

  python launcher.py
  → http://127.0.0.1:5055/
"""

from __future__ import annotations

import json
import os
import signal
import subprocess
import sys
import threading
import time
from collections import deque
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from flask import Flask, Response, jsonify, request, send_from_directory

ROOT = Path(__file__).resolve().parent
PROMPTS_PATH = ROOT / "prompts.json"
HUB_HOST = "127.0.0.1"
HUB_PORT = 5055

app = Flask(__name__, static_folder=None)


@dataclass
class DemoRuntime:
    project_id: str
    process: subprocess.Popen | None = None
    logs: deque = field(default_factory=lambda: deque(maxlen=4000))
    steps: dict[str, str] = field(
        default_factory=lambda: {
            "venv": "off",
            "deps": "off",
            "db": "off",
            "api": "off",
            "frontend": "off",
        }
    )
    status: str = "stopped"  # stopped | starting | running | error
    started_at: float | None = None
    url: str = "http://127.0.0.1:5000/"
    api_health: str = "http://127.0.0.1:5000/api/health"
    _lock: threading.Lock = field(default_factory=threading.Lock)
    _reader: threading.Thread | None = None
    _health: threading.Thread | None = None
    _stop_health: threading.Event = field(default_factory=threading.Event)


RUNTIMES: dict[str, DemoRuntime] = {}
RUNTIMES_LOCK = threading.Lock()


def project_abs_path(project_id: str) -> str:
    return str((ROOT / project_id).resolve())


def _substitute_paths(obj: Any, project_id: str) -> Any:
    """Replace {{PROJECT_PATH}} with the absolute path for this machine/clone."""
    token = "{{PROJECT_PATH}}"
    abs_path = project_abs_path(project_id)
    if isinstance(obj, str):
        return obj.replace(token, abs_path)
    if isinstance(obj, list):
        return [_substitute_paths(x, project_id) for x in obj]
    if isinstance(obj, dict):
        return {k: _substitute_paths(v, project_id) for k, v in obj.items()}
    return obj


def load_prompts() -> dict[str, Any]:
    if not PROMPTS_PATH.exists():
        return {}
    raw = json.loads(PROMPTS_PATH.read_text(encoding="utf-8"))
    out: dict[str, Any] = {}
    for pid, meta in raw.items():
        out[pid] = _substitute_paths(meta, pid)
    return out


def discover_demos() -> list[dict[str, Any]]:
    prompts = load_prompts()
    demos: list[dict[str, Any]] = []
    for child in sorted(ROOT.iterdir()):
        if not child.is_dir():
            continue
        setup = child / "setup_and_run.py"
        if not setup.exists():
            continue
        pid = child.name
        meta = prompts.get(pid, {})
        with RUNTIMES_LOCK:
            rt = RUNTIMES.get(pid)
        demos.append(
            {
                "id": pid,
                "name": meta.get("label") or pid.replace("-", " ").replace("_", " ").title(),
                "path": str(child.resolve()),
                "has_prompts": bool(meta.get("usecases")),
                "usecase_count": len(meta.get("usecases") or []),
                "url": meta.get("app_url") or "http://127.0.0.1:5000/",
                "api_health": meta.get("api_health") or "http://127.0.0.1:5000/api/health",
                "status": rt.status if rt else "stopped",
                "steps": dict(rt.steps) if rt else {
                    "venv": "off",
                    "deps": "off",
                    "db": "off",
                    "api": "off",
                    "frontend": "off",
                },
            }
        )
    return demos


def append_log(rt: DemoRuntime, line: str) -> None:
    ts = time.strftime("%H:%M:%S")
    msg = line.rstrip("\n")
    with rt._lock:
        rt.logs.append(f"[{ts}] {msg}")
    _infer_steps(rt, msg)


def _infer_steps(rt: DemoRuntime, msg: str) -> None:
    low = msg.lower()
    with rt._lock:
        if "creating virtualenv" in low or "using existing virtualenv" in low:
            rt.steps["venv"] = "pending" if "creating" in low else "ok"
        if "venv" in low and ("created" in low or "using existing" in low):
            rt.steps["venv"] = "ok"
        if "pip install" in low or "upgrading pip" in low or "-m pip" in low:
            rt.steps["deps"] = "pending"
        if "successfully installed" in low or ("requirement already satisfied" in low and rt.steps["deps"] != "ok"):
            # stay pending until batch finishes; mark ok on "Initializing SQLite"
            pass
        if "initializing sqlite" in low:
            rt.steps["deps"] = "ok"
            rt.steps["db"] = "pending"
            if rt.steps["venv"] != "ok":
                rt.steps["venv"] = "ok"
        if "db ready" in low:
            rt.steps["db"] = "ok"
        if "running on http" in low or "press ctrl+c" in low or "frontend :" in low:
            if rt.steps["db"] == "pending":
                rt.steps["db"] = "ok"
            if rt.steps["deps"] != "ok":
                rt.steps["deps"] = "ok"
            if rt.steps["venv"] != "ok":
                rt.steps["venv"] = "ok"
            rt.steps["api"] = "pending"
            rt.steps["frontend"] = "pending"
            rt.status = "running"


def _reader_loop(rt: DemoRuntime) -> None:
    assert rt.process is not None
    stream = rt.process.stdout
    if stream is None:
        return
    for raw in iter(stream.readline, ""):
        if raw == "":
            break
        append_log(rt, raw)
    code = rt.process.poll()
    if code is not None and code != 0:
        with rt._lock:
            if rt.status != "stopped":
                rt.status = "error"
        append_log(rt, f"Process exited with code {code}")
    elif code == 0:
        with rt._lock:
            if rt.status == "running":
                rt.status = "stopped"
                for k in rt.steps:
                    if rt.steps[k] == "pending":
                        rt.steps[k] = "off"
        append_log(rt, "Process exited cleanly.")


def _health_loop(rt: DemoRuntime) -> None:
    import urllib.request

    while not rt._stop_health.wait(1.5):
        if rt.status not in ("starting", "running"):
            continue
        api_ok = False
        front_ok = False
        try:
            with urllib.request.urlopen(rt.api_health, timeout=1.5) as resp:
                api_ok = 200 <= resp.status < 500
        except Exception:
            api_ok = False
        try:
            with urllib.request.urlopen(rt.url, timeout=1.5) as resp:
                front_ok = 200 <= resp.status < 500
        except Exception:
            front_ok = False
        with rt._lock:
            if api_ok:
                rt.steps["api"] = "ok"
            elif rt.steps["api"] == "ok":
                rt.steps["api"] = "pending"
            if front_ok:
                rt.steps["frontend"] = "ok"
            elif rt.steps["frontend"] == "ok":
                rt.steps["frontend"] = "pending"
            if api_ok and front_ok:
                rt.status = "running"


def stop_demo(project_id: str) -> None:
    with RUNTIMES_LOCK:
        rt = RUNTIMES.get(project_id)
    if not rt:
        return
    rt._stop_health.set()
    proc = rt.process
    if proc and proc.poll() is None:
        append_log(rt, "Stopping demo…")
        try:
            if sys.platform == "win32":
                subprocess.call(
                    ["taskkill", "/PID", str(proc.pid), "/T", "/F"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
            else:
                os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
        except Exception as e:
            append_log(rt, f"Stop warning: {e}")
            try:
                proc.kill()
            except Exception:
                pass
        try:
            proc.wait(timeout=5)
        except Exception:
            pass
    with rt._lock:
        rt.status = "stopped"
        rt.process = None
        for k in list(rt.steps):
            rt.steps[k] = "off"
    append_log(rt, "Demo stopped.")


def launch_demo(project_id: str) -> DemoRuntime:
    demo_dir = ROOT / project_id
    setup = demo_dir / "setup_and_run.py"
    if not setup.exists():
        raise FileNotFoundError(f"No setup_and_run.py in {demo_dir}")

    prompts = load_prompts().get(project_id, {})

    with RUNTIMES_LOCK:
        existing = RUNTIMES.get(project_id)
        if existing and existing.process and existing.process.poll() is None:
            raise RuntimeError("Demo already running")
        for other_id, other in list(RUNTIMES.items()):
            if other_id != project_id and other.status in ("starting", "running"):
                stop_demo(other_id)

        rt = DemoRuntime(
            project_id=project_id,
            url=prompts.get("app_url") or "http://127.0.0.1:5000/",
            api_health=prompts.get("api_health") or "http://127.0.0.1:5000/api/health",
        )
        RUNTIMES[project_id] = rt

    append_log(rt, f"Launching {project_id}")
    append_log(rt, f"Working directory: {demo_dir}")
    with rt._lock:
        rt.status = "starting"
        rt.started_at = time.time()
        for k in rt.steps:
            rt.steps[k] = "off"
        rt.steps["venv"] = "pending"

    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"
    env["PIP_DISABLE_PIP_VERSION_CHECK"] = "1"

    creationflags = 0
    if sys.platform == "win32":
        creationflags = subprocess.CREATE_NEW_PROCESS_GROUP  # type: ignore[attr-defined]

    proc = subprocess.Popen(
        [sys.executable, "-u", str(setup)],
        cwd=str(demo_dir),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        env=env,
        creationflags=creationflags,
    )
    rt.process = proc
    rt._stop_health.clear()
    rt._reader = threading.Thread(target=_reader_loop, args=(rt,), daemon=True)
    rt._health = threading.Thread(target=_health_loop, args=(rt,), daemon=True)
    rt._reader.start()
    rt._health.start()
    return rt


@app.get("/")
def index():
    return send_from_directory(ROOT, "index.html")


@app.get("/api/demos")
def api_demos():
    return jsonify({"demos": discover_demos()})


@app.get("/api/prompts")
def api_prompts():
    project = request.args.get("project")
    data = load_prompts()
    if project:
        if project not in data:
            return jsonify({"error": "unknown project", "usecases": []}), 404
        return jsonify({"project": project, **data[project]})
    return jsonify({"projects": data})


@app.get("/api/status/<project_id>")
def api_status(project_id: str):
    with RUNTIMES_LOCK:
        rt = RUNTIMES.get(project_id)
    if not rt:
        return jsonify(
            {
                "project": project_id,
                "status": "stopped",
                "steps": {
                    "venv": "off",
                    "deps": "off",
                    "db": "off",
                    "api": "off",
                    "frontend": "off",
                },
                "url": None,
            }
        )
    with rt._lock:
        return jsonify(
            {
                "project": project_id,
                "status": rt.status,
                "steps": dict(rt.steps),
                "url": rt.url,
                "api_health": rt.api_health,
                "pid": rt.process.pid if rt.process else None,
            }
        )


@app.get("/api/logs/<project_id>")
def api_logs(project_id: str):
    after = int(request.args.get("after", 0))
    with RUNTIMES_LOCK:
        rt = RUNTIMES.get(project_id)
    if not rt:
        return jsonify({"lines": [], "next": 0, "status": "stopped"})
    with rt._lock:
        lines = list(rt.logs)
        chunk = lines[after:]
        return jsonify(
            {
                "lines": chunk,
                "next": len(lines),
                "status": rt.status,
                "steps": dict(rt.steps),
            }
        )


@app.post("/api/launch/<project_id>")
def api_launch(project_id: str):
    try:
        rt = launch_demo(project_id)
    except FileNotFoundError as e:
        return jsonify({"ok": False, "error": str(e)}), 404
    except RuntimeError as e:
        return jsonify({"ok": False, "error": str(e)}), 409
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500
    return jsonify({"ok": True, "project": project_id, "status": rt.status, "url": rt.url})


@app.post("/api/stop/<project_id>")
def api_stop(project_id: str):
    stop_demo(project_id)
    return jsonify({"ok": True, "project": project_id, "status": "stopped"})


@app.get("/api/events/<project_id>")
def api_events(project_id: str):
    def stream():
        cursor = 0
        while True:
            with RUNTIMES_LOCK:
                rt = RUNTIMES.get(project_id)
            if not rt:
                yield f"data: {json.dumps({'status': 'stopped', 'lines': [], 'steps': {}})}\n\n"
                time.sleep(1)
                continue
            with rt._lock:
                lines = list(rt.logs)
                chunk = lines[cursor:]
                cursor = len(lines)
                payload = {
                    "status": rt.status,
                    "steps": dict(rt.steps),
                    "lines": chunk,
                    "url": rt.url,
                }
            yield f"data: {json.dumps(payload)}\n\n"
            if rt.status in ("stopped", "error") and not chunk:
                time.sleep(1.2)
            else:
                time.sleep(0.4)

    return Response(
        stream(),
        mimetype="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


def main() -> None:
    print("==============================================")
    print(" Demo Projects Hub")
    print(f" Dashboard : http://{HUB_HOST}:{HUB_PORT}/")
    print(f" Root      : {ROOT}")
    print("==============================================")
    app.run(host=HUB_HOST, port=HUB_PORT, debug=False, threaded=True, use_reloader=False)


if __name__ == "__main__":
    main()
