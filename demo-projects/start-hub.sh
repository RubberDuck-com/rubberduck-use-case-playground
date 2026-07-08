#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

if ! command -v python3 >/dev/null 2>&1 && ! command -v python >/dev/null 2>&1; then
  echo "ERROR: Python was not found on PATH."
  echo "Install Python 3 and try again."
  exit 1
fi

PYTHON=python3
command -v python3 >/dev/null 2>&1 || PYTHON=python

if ! "$PYTHON" -c "import flask" >/dev/null 2>&1; then
  echo "Installing Flask for the demo hub..."
  "$PYTHON" -m pip install flask
fi

echo
echo "Starting Demo Projects Hub..."
echo "Open http://127.0.0.1:5055/ in your browser."
echo "Press Ctrl+C to stop."
echo
exec "$PYTHON" launcher.py
