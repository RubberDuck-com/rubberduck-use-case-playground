#!/usr/bin/env python3
"""One-command lab launcher for RubberDuck use-case playground."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "labs" / "manifest.json"
VENV = ROOT / ".venv"


def load_manifest() -> dict:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def python_exe() -> str:
    if sys.platform == "win32":
        cand = VENV / "Scripts" / "python.exe"
    else:
        cand = VENV / "bin" / "python"
    return str(cand) if cand.exists() else sys.executable


def ensure_venv() -> None:
    if not VENV.exists():
        print("Creating .venv ...")
        subprocess.check_call([sys.executable, "-m", "venv", str(VENV)], cwd=ROOT)
    subprocess.check_call([python_exe(), "-m", "pip", "install", "-q", "-r", "requirements.txt"], cwd=ROOT)
    subprocess.check_call([python_exe(), "-m", "pip", "install", "-q", "-e", "."], cwd=ROOT)
    if not (VENV / ".rd-lab-ready").exists():
        (VENV / ".rd-lab-ready").write_text("ok", encoding="utf-8")
        print("Dependencies installed.\n")


def lab_env() -> dict:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT)
    return env


def run_verify(lab: dict) -> None:
    cmd = lab.get("verify")
    if not cmd:
        return
    print(f"Running verify: {cmd}\n")
    if cmd.startswith("pytest"):
        subprocess.check_call([python_exe(), "-m", *cmd.split()], cwd=ROOT, env=lab_env())
    elif cmd.startswith("python "):
        script = cmd.split("python ", 1)[1]
        subprocess.check_call([python_exe(), script], cwd=ROOT, env=lab_env())
    else:
        subprocess.check_call(cmd, shell=True, cwd=ROOT, env=lab_env())


def read_prompt(uc_id: str) -> str:
    """Extract the pre-filled Playground prompt from docs/uc-XX.md."""
    path = ROOT / "docs" / f"uc-{uc_id}.md"
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    marker = "## Playground prompt"
    if marker not in text:
        return ""
    rest = text.split(marker, 1)[1]
    for fence in ("````", "```"):
        if fence in rest:
            block = rest.split(fence, 2)[1]
            if block.startswith("\n"):
                block = block[1:]
            return block.split(fence, 1)[0].strip()
    return ""


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run a RubberDuck UC lab: demo + copy-paste prompt",
        epilog="Default: run the live demo and print the Cursor prompt. "
        "Use --verify for pytest smoke tests, --server for UC-02 API.",
    )
    parser.add_argument("--uc", required=True, help="Use case number 01-10")
    parser.add_argument("--setup-only", action="store_true", help="Install venv only")
    parser.add_argument("--verify", action="store_true", help="Run lab verify script (pytest)")
    parser.add_argument("--no-run", action="store_true", help="Skip the live demo (prompt only)")
    parser.add_argument("--server", "--start-server", dest="start_server", action="store_true",
                        help="Start lab server (UC-02 API on :8080)")
    args = parser.parse_args()

    uc_key = args.uc.zfill(2)
    data = load_manifest()
    lab = data["labs"].get(uc_key)
    if not lab:
        print(f"Unknown UC: {args.uc}", file=sys.stderr)
        return 1

    ensure_venv()
    if args.setup_only:
        return 0

    repo_path = str(ROOT.resolve())
    print("=" * 60)
    print(f"UC-{uc_key}: {lab['title']}")
    print(f"Lab folder: {lab['project_dir']}")
    print("=" * 60)

    if not args.no_run and not args.start_server:
        print("\n--- Step 1: Live demo (terminal) ---\n")
        subprocess.check_call([python_exe(), "scripts/demo.py", uc_key], cwd=ROOT, env=lab_env())
        print()

    if args.verify and lab.get("verify"):
        print("--- Verify (pytest smoke test) ---\n")
        run_verify(lab)
        print()

    if args.start_server and lab.get("start"):
        cmd = lab["start"]
        print(f"Starting server (Ctrl+C to stop):\n  {cmd}\n")
        if lab.get("url"):
            print(f"Open: {lab['url']}\n")
        parts = cmd.split()
        subprocess.call([python_exe(), "-m", *parts], cwd=ROOT, env=lab_env())
        return 0

    prompt = read_prompt(uc_key)
    print("--- Step 2: Index in RubberDuck (once per session) ---\n")
    print(data["setup"]["index_prompt"].format(repo_path=repo_path))
    print("\n--- Step 3: Copy this prompt into Cursor chat ---\n")
    print(prompt or f"(open docs/uc-{uc_key}.md and copy the Playground prompt block)")
    print("\n--- Focus files ---\n")
    for p in lab.get("focus_paths", []):
        print(f"  - {p}")
    print("\nFull guide: docs/HOW_TO_TEST.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
