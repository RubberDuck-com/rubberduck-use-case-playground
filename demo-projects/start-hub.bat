@echo off
setlocal
cd /d "%~dp0"

where python >nul 2>&1
if errorlevel 1 (
  echo ERROR: Python was not found on PATH.
  echo Install Python 3 and try again.
  pause
  exit /b 1
)

python -c "import flask" >nul 2>&1
if errorlevel 1 (
  echo Installing Flask for the demo hub...
  python -m pip install flask
  if errorlevel 1 (
    echo ERROR: could not install flask.
    pause
    exit /b 1
  )
)

echo.
echo Starting Demo Projects Hub...
echo Open http://127.0.0.1:5055/ in your browser.
echo Press Ctrl+C to stop.
echo.
python launcher.py
pause
