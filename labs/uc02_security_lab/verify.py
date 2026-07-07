"""UC-02: start API and hit endpoints."""
import os
import subprocess
import sys
import time
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parents[2]
BASE = "http://127.0.0.1:8080"


def main() -> None:
  env = os.environ.copy()
  env["PYTHONPATH"] = str(ROOT) + os.pathsep + env.get("PYTHONPATH", "")
  proc = subprocess.Popen(
      [sys.executable, "-m", "uvicorn", "demoapp.api.server:app", "--host", "127.0.0.1", "--port", "8080"],
      stdout=subprocess.DEVNULL,
      stderr=subprocess.DEVNULL,
      env=env,
      cwd=str(ROOT),
  )
  try:
      for _ in range(30):
          try:
              r = httpx.get(f"{BASE}/health", timeout=1.0)
              if r.status_code == 200:
                  break
          except httpx.HTTPError:
              time.sleep(0.2)
      else:
          raise SystemExit("API did not start")
      assert httpx.get(f"{BASE}/api/profiles").status_code == 401
      assert httpx.get(f"{BASE}/api/search", params={"q": "test"}).status_code == 200
      print("UC-02 lab OK: API running, auth enforced, search endpoint open")
  finally:
      proc.terminate()
      proc.wait(timeout=5)


if __name__ == "__main__":
  main()
