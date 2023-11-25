import os
import sys
import subprocess
import time

def open_cmd_window(folder_path):

    # Determine the platform
    platform = sys.platform

    # Use the appropriate command based on the platform
    if platform == "win32":
        cmd_command = f'start cmd /K cd /D "{folder_path}"'
    else:
        print(f"Error: {e}")

    try:
        subprocess.Popen(cmd_command, shell=True)
         # Wait for a short duration (e.g., 2 seconds) for the command prompt to open
        time.sleep(2)

        # Add a cleanup command (e.g., 'cls' to clear the command prompt)
        cleanup_command = 'cls'
        subprocess.run(cleanup_command, shell=True)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    open_cmd_window(sys.argv[1])
