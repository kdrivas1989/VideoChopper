@echo off
echo Starting Video Chopper...
echo.
echo Opening http://localhost:8080 in your browser...
echo.
echo (Keep this window open while using the app)
echo (Press Ctrl+C to stop)
echo.

:: Open browser after a short delay
start "" "http://localhost:8080"

:: Run the app
python main.py
