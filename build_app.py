#!/usr/bin/env python3
"""Build script to create standalone Video Chopper app."""

import subprocess
import sys
import os
import shutil

def create_icns():
    """Create macOS .icns file from PNG."""
    if sys.platform != 'darwin':
        return None

    png_path = 'static/icon-512.png'
    if not os.path.exists(png_path):
        return None

    iconset_path = 'VideoChopper.iconset'
    icns_path = 'VideoChopper.icns'

    # Create iconset directory
    os.makedirs(iconset_path, exist_ok=True)

    # Generate different icon sizes
    sizes = [16, 32, 64, 128, 256, 512]
    for size in sizes:
        # Regular size
        subprocess.run([
            'sips', '-z', str(size), str(size), png_path,
            '--out', f'{iconset_path}/icon_{size}x{size}.png'
        ], capture_output=True)
        # @2x size (retina)
        if size <= 256:
            subprocess.run([
                'sips', '-z', str(size*2), str(size*2), png_path,
                '--out', f'{iconset_path}/icon_{size}x{size}@2x.png'
            ], capture_output=True)

    # Convert iconset to icns
    subprocess.run(['iconutil', '-c', 'icns', iconset_path], capture_output=True)

    # Clean up iconset
    shutil.rmtree(iconset_path, ignore_errors=True)

    return icns_path if os.path.exists(icns_path) else None

def build():
    """Build the standalone app using PyInstaller."""

    # Determine path separator for --add-data (: on macOS/Linux, ; on Windows)
    sep = ';' if sys.platform == 'win32' else ':'

    # Create macOS icon if possible
    icns_path = create_icns()

    # PyInstaller command
    cmd = [
        sys.executable, '-m', 'PyInstaller',
        '--name=Video Chopper',
        '--windowed',  # No console window
        '--onedir',    # Create a directory with all files
        f'--add-data=templates{sep}templates',  # Include templates folder
        f'--add-data=static{sep}static',        # Include static folder
        '--hidden-import=moviepy',
        '--hidden-import=imageio',
        '--hidden-import=imageio_ffmpeg',
        '--hidden-import=flask',
        '--hidden-import=werkzeug',
        '--hidden-import=webview',
        '--collect-all=moviepy',
        '--collect-all=imageio',
        '--collect-all=imageio_ffmpeg',
        '--collect-all=webview',
        '--copy-metadata=imageio',
        '--copy-metadata=imageio_ffmpeg',
        '--noconfirm',  # Replace output without asking
        'app.py'
    ]

    # Add icon
    if sys.platform == 'darwin' and icns_path:
        cmd.insert(-1, f'--icon={icns_path}')
    elif sys.platform == 'win32' and os.path.exists('icon.ico'):
        cmd.insert(-1, '--icon=icon.ico')

    print("=" * 50)
    print("Building Video Chopper app...")
    print("This may take several minutes...")
    print("=" * 50)

    result = subprocess.run(cmd, cwd=os.path.dirname(os.path.abspath(__file__)) or '.')

    # Clean up icns file
    if icns_path and os.path.exists(icns_path):
        os.remove(icns_path)

    if result.returncode == 0:
        print("\n" + "=" * 50)
        print("BUILD COMPLETE!")
        print("=" * 50)
        if sys.platform == 'darwin':
            app_path = "dist/Video Chopper.app"
            if os.path.exists(app_path):
                print(f"\nApp created: {app_path}")
                print("\nTo run: open 'dist/Video Chopper.app'")
                print("\nTo install: drag 'Video Chopper.app' to Applications folder")
            else:
                print("\nApp location: dist/Video Chopper/")
        elif sys.platform == 'win32':
            print("\nApp location: dist\\Video Chopper\\Video Chopper.exe")
        else:
            print("\nApp location: dist/Video Chopper/Video Chopper")
    else:
        print("\n✗ Build failed")
        return 1

    return 0

if __name__ == '__main__':
    sys.exit(build())
