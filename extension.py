import os
import sys
import subprocess
import time

def open_cmd_window(folder_path):
    platform = sys.platform

    if platform == "win32":
        cmd_command = f'start cmd /K cd /D "{folder_path}"'
        cleanup_command = 'cls'
    elif platform == "darwin":
        cmd_command = f'open "{folder_path}"'
        cleanup_command = 'clear'
    elif platform.startswith("linux"):
        cmd_command = f'xdg-open "{folder_path}"'
        cleanup_command = 'clear'
    else:
        print(f"Unsupported platform: {platform}")
        return

    try:
        subprocess.Popen(cmd_command, shell=True)
        time.sleep(2)
        subprocess.run(cleanup_command, shell=True)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    open_cmd_window(sys.argv[1])
