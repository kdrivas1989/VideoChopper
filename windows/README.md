# Video Chopper for Windows

A desktop application for trimming video files into segments with custom naming.

## Requirements

- **Python 3.9+** - Download from [python.org](https://python.org)
- **FFmpeg** - Required for video processing

### Installing FFmpeg on Windows

1. Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html) or use a package manager:
   ```
   winget install ffmpeg
   ```
   or
   ```
   choco install ffmpeg
   ```

2. Make sure `ffmpeg` and `ffprobe` are in your system PATH.

## Quick Start

### Option 1: Run with Python (Recommended)

1. Double-click `run.bat` to start the app with a native window
2. Or double-click `run_browser.bat` to open in your default browser

The first run will:
- Create a virtual environment
- Install all required dependencies
- Start the application

### Option 2: Build Standalone Executable

1. Install PyInstaller: `pip install pyinstaller`
2. Run: `python build_windows.py`
3. Find the executable in `dist/VideoChopper/VideoChopper.exe`

**Note:** Copy `ffmpeg.exe` and `ffprobe.exe` to the `dist/VideoChopper` folder if they're not in your system PATH.

## Features

- Drag & drop video files (MP4, AVI, MOV, MKV, WMV, FLV, WebM, MTS)
- Preview videos with keyboard shortcuts
- Define multiple trim segments per video
- Custom filename format: `Competition_Team#_Round#.mp4`
- Optional competition name prefix
- Custom save folder location
- Export segment data to CSV

## Keyboard Shortcuts (Preview Mode)

| Key | Action |
|-----|--------|
| 1-9, 0 | Select segment 1-10 |
| S | Set start time at current position |
| E | Set end time at current position |
| T | Save & Trim all segments |
| Space | Play/Pause |
| ← / → | Skip 5 seconds back/forward |
| Escape | Close preview |

## Troubleshooting

### "Python is not installed"
Download and install Python from [python.org](https://python.org). Make sure to check "Add Python to PATH" during installation.

### "ffmpeg not found"
Install FFmpeg and ensure it's in your system PATH. You can verify by running `ffmpeg -version` in Command Prompt.

### Video won't play in preview
Some video codecs (like HEVC/H.265) aren't supported by browsers. The app will automatically transcode these to H.264 for preview. Wait for the "Preview ready" status.

## Data Location

App data is stored in:
- `%LOCALAPPDATA%\VideoChopper\uploads` - Uploaded videos
- `%LOCALAPPDATA%\VideoChopper\output` - Trimmed segments
- `%LOCALAPPDATA%\VideoChopper\previews` - Transcoded previews

Default save folder: `%USERPROFILE%\Downloads\VideoChopper`
