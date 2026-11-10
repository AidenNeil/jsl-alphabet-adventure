"""Script to start the Flask server and automatically open the browser"""
import webbrowser
import time
import threading
import os
import sys

def open_browser():
    """Wait a moment then open the browser"""
    time.sleep(1.5)  # Wait for server to start
    print("\n[BROWSER] Opening browser...")
    webbrowser.open('http://localhost:7000')

def main():
    """Start server and open browser"""
    # Start browser in a separate thread
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Start the Flask app
    from app import app
    
    PORT = 7000
    print("\n" + "="*60)
    print("JSL Alphabet Adventure - Web Version")
    print("="*60)
    print("\nStarting web server...")
    print("\n[BROWSER] Browser will open automatically...")
    print("\nIf it doesn't open, go to:")
    print(f"  http://localhost:{PORT}")
    print("\nPress CTRL+C to stop the server")
    print("="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=PORT, use_reloader=False)

if __name__ == '__main__':
    main()

