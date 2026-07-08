"""
One-shot setup + run for rubberduck_pizzeria-demoapp.

Starts everything in one process:
  - SQLite DB  (creates/seeds package/rubber_duck_pizzeria/data/pizzeria.db)
  - Kitchen API  (/api/*)
  - Frontend UI  (http://127.0.0.1:5000/)

Usage (from this folder):
  python setup_and_run.py

Stop with Ctrl+C.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# App lives in package/ when root is the demo folder; otherwise this file sits next to main.py.
if (ROOT / "package" / "main.py").exists():
    APP_DIR = ROOT / "package"
elif (ROOT / "main.py").exists():
    APP_DIR = ROOT
else:
    print("ERROR: cannot find main.py (looked in ./package and .)", file=sys.stderr)
    sys.exit(1)

REQUIREMENTS = APP_DIR / "requirements.txt"
VENV_DIR = APP_DIR / ".venv"


def venv_python() -> Path:
    if sys.platform == "win32":
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"


def run(cmd: list[str], *, cwd: Path | None = None) -> None:
    print(f"\n>>> {' '.join(cmd)}")
    subprocess.check_call(cmd, cwd=str(cwd or APP_DIR))


def ensure_venv() -> Path:
    py = venv_python()
    if not py.exists():
        print(f"Creating virtualenv at {VENV_DIR} ...")
        run([sys.executable, "-m", "venv", str(VENV_DIR)], cwd=APP_DIR)
    else:
        print(f"Using existing virtualenv: {VENV_DIR}")
    if not py.exists():
        raise SystemExit(f"venv python not found: {py}")
    return py


def install_deps(py: Path) -> None:
    if not REQUIREMENTS.exists():
        raise SystemExit(f"Missing requirements file: {REQUIREMENTS}")
    run([str(py), "-m", "pip", "install", "--upgrade", "pip"])
    run([str(py), "-m", "pip", "install", "-r", str(REQUIREMENTS)])


def init_database(py: Path) -> None:
    """Create SQLite schema + seed data before the web server starts."""
    print("\n>>> Initializing SQLite database ...")
    code = (
        "from rubber_duck_pizzeria import db as dbmod; "
        "dbmod.init_db(force=False); "
        "print('DB ready:', dbmod.DB_PATH)"
    )
    subprocess.check_call([str(py), "-c", code], cwd=str(APP_DIR))


def start_server(py: Path) -> int:
    main = APP_DIR / "main.py"
    if not main.exists():
        raise SystemExit(f"Missing {main}")
    print("\n==============================================")
    print(" rubberduck_pizzeria-demoapp")
    print(" Frontend : http://127.0.0.1:5000/")
    print(" API      : http://127.0.0.1:5000/api/health")
    print(" Database : package/rubber_duck_pizzeria/data/pizzeria.db")
    print("==============================================")
    print("Press Ctrl+C to stop.\n")
    return subprocess.call([str(py), str(main)], cwd=str(APP_DIR))


def main() -> int:
    print(f"Demo root : {ROOT}")
    print(f"App dir   : {APP_DIR}")
    py = ensure_venv()
    install_deps(py)
    init_database(py)
    return start_server(py)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("\nStopped.")
        raise SystemExit(0)
    except subprocess.CalledProcessError as e:
        print(f"\nCommand failed with exit code {e.returncode}", file=sys.stderr)
        raise SystemExit(e.returncode)
