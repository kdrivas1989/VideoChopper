#!/usr/bin/env python3
"""Video Chopper Desktop App - Windows Version with native window."""

import threading
import webbrowser
import sys
import os

# Add the current directory to path for imports
if getattr(sys, 'frozen', False):
    # Running as compiled executable
    os.chdir(sys._MEIPASS)

from main import app

USE_BROWSER = '--browser' in sys.argv

def start_server():
    """Start Flask server."""
    # Suppress Flask logs in production
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    app.run(host='127.0.0.1', port=5050, debug=False, use_reloader=False, threaded=True)

if __name__ == '__main__':
    if USE_BROWSER:
        # Open in default browser
        import time
        server_thread = threading.Thread(target=start_server, daemon=True)
        server_thread.start()
        time.sleep(1.5)  # Wait for server to start
        webbrowser.open('http://127.0.0.1:5050')
        print("Video Chopper running at http://127.0.0.1:5050")
        print("Press Ctrl+C to stop")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nStopping...")
    else:
        # Use pywebview (native window)
        try:
            import webview
            server_thread = threading.Thread(target=start_server, daemon=True)
            server_thread.start()

            window = webview.create_window(
                'Video Chopper',
                'http://127.0.0.1:5050',
                width=1200,
                height=800,
                resizable=True,
                min_size=(800, 600)
            )
            webview.start(private_mode=False)
        except ImportError:
            # Fallback to browser if pywebview not installed
            print("pywebview not installed, opening in browser...")
            import time
            server_thread = threading.Thread(target=start_server, daemon=True)
            server_thread.start()
            time.sleep(1.5)
            webbrowser.open('http://127.0.0.1:5050')
            print("Video Chopper running at http://127.0.0.1:5050")
            print("Press Ctrl+C to stop")
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\nStopping...")
