@echo off
echo ========================================
echo    Video Chopper - Windows Setup
echo ========================================
echo.

:: Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed!
    echo.
    echo Please install Python from: https://python.org
    echo IMPORTANT: Check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b 1
)
echo [OK] Python found

:: Check for ffmpeg
ffmpeg -version >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] ffmpeg not found. Attempting to install...
    echo.

    :: Try winget first
    winget install ffmpeg >nul 2>&1
    if %errorlevel% neq 0 (
        echo [ERROR] Could not install ffmpeg automatically.
        echo.
        echo Please install ffmpeg manually:
        echo 1. Download from: https://ffmpeg.org/download.html
        echo 2. Or run: winget install ffmpeg
        echo 3. Make sure ffmpeg is in your PATH
        echo.
        pause
        exit /b 1
    )
    echo [OK] ffmpeg installed
) else (
    echo [OK] ffmpeg found
)

:: Install Python dependencies
echo.
echo Installing Python dependencies...
pip install flask moviepy imageio imageio-ffmpeg gunicorn boto3 botocore --quiet
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)
echo [OK] Dependencies installed

:: Create necessary folders
if not exist "%USERPROFILE%\VideoChopper" mkdir "%USERPROFILE%\VideoChopper"
if not exist "%USERPROFILE%\VideoChopper\uploads" mkdir "%USERPROFILE%\VideoChopper\uploads"
if not exist "%USERPROFILE%\VideoChopper\output" mkdir "%USERPROFILE%\VideoChopper\output"
if not exist "%USERPROFILE%\VideoChopper\previews" mkdir "%USERPROFILE%\VideoChopper\previews"

echo.
echo ========================================
echo    Setup Complete!
echo ========================================
echo.
echo To run Video Chopper, double-click: run-video-chopper.bat
echo.
pause
