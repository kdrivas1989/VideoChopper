@echo off
title Video Chopper (Browser Mode)
echo Starting Video Chopper in browser mode...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH.
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Check if running from the correct directory
if not exist "app.py" (
    echo Error: app.py not found. Please run this from the Video Chopper directory.
    pause
    exit /b 1
)

REM Install dependencies if needed
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo Installing dependencies...
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate.bat
)

REM Run the app in browser mode
python app.py --browser

pause
