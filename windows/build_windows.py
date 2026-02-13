#!/usr/bin/env python3
"""Build Video Chopper as a Windows executable using PyInstaller."""

import os
import sys
import subprocess
import shutil

def build():
    """Build the Windows executable."""
    print("=== Building Video Chopper for Windows ===\n")

    # Check for PyInstaller
    try:
        import PyInstaller
    except ImportError:
        print("PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyinstaller'])

    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # Clean previous builds
    for folder in ['build', 'dist']:
        if os.path.exists(folder):
            print(f"Cleaning {folder}...")
            shutil.rmtree(folder)

    # PyInstaller command
    cmd = [
        sys.executable, '-m', 'PyInstaller',
        '--name=VideoChopper',
        '--onedir',
        '--windowed',
        '--noconfirm',
        '--clean',

        # Add data files
        '--add-data=templates;templates',
        '--add-data=static;static',

        # Hidden imports for Flask and moviepy
        '--hidden-import=flask',
        '--hidden-import=werkzeug',
        '--hidden-import=jinja2',
        '--hidden-import=moviepy',
        '--hidden-import=moviepy.editor',
        '--hidden-import=imageio',
        '--hidden-import=imageio_ffmpeg',
        '--hidden-import=imageio_ffmpeg.binaries',
        '--hidden-import=numpy',
        '--hidden-import=webview',
        '--hidden-import=webview.platforms.winforms',
        '--hidden-import=clr_loader',
        '--hidden-import=pythonnet',

        # Collect all packages needed
        '--collect-all=moviepy',
        '--collect-all=imageio',
        '--collect-all=imageio_ffmpeg',
        '--collect-all=webview',

        # Entry point
        'app.py'
    ]

    print("Running PyInstaller...")
    print(" ".join(cmd))
    print()

    result = subprocess.run(cmd)

    if result.returncode == 0:
        print("\n=== Build Successful! ===")
        print(f"Executable located at: {os.path.join(script_dir, 'dist', 'VideoChopper', 'VideoChopper.exe')}")
        print("\nNote: Make sure ffmpeg.exe and ffprobe.exe are in your system PATH")
        print("or copy them to the dist/VideoChopper folder.")
    else:
        print("\n=== Build Failed ===")
        sys.exit(1)

if __name__ == '__main__':
    build()
