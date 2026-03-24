"""
Force restart server to clear cache
"""

import os
import sys
import subprocess

def restart_server():
    """Force restart the server"""
    print("🔄 Stopping any existing server processes...")
    
    # Kill any existing Python processes on port 8000
    try:
        if os.name == 'nt':  # Windows
            subprocess.run(['taskkill', '/F', '/IM', 'python.exe'], capture_output=True)
        else:  # Unix/Linux/Mac
            subprocess.run(['pkill', '-f', 'python'], capture_output=True)
    except:
        pass
    
    print("🚀 Starting fresh server...")
    
    # Start the server
    try:
        subprocess.run([sys.executable, 'main.py'], cwd='.')
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")

if __name__ == "__main__":
    restart_server()
