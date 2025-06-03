import os
import platform
import subprocess

def print_system_uptime():
    """
    Prints the system uptime in a human-readable format.
    Works on Linux, macOS, and Windows.
    """
    try:
        system = platform.system()
        if system == "Linux":
            # Use the uptime command
            uptime = subprocess.check_output(['uptime', '-p'], encoding='utf-8').strip()
            print(f"System uptime: {uptime}")
        elif system == "Darwin":
            # macOS also supports `uptime`
            uptime = subprocess.check_output(['uptime'], encoding='utf-8').strip()
            print(f"System uptime: {uptime}")
        elif system == "Windows":
            # Use WMIC to get uptime in seconds
            import ctypes
            from datetime import timedelta

            lib = ctypes.windll.kernel32
            ticks = lib.GetTickCount64()
            uptime_seconds = int(ticks // 1000)
            uptime_str = str(timedelta(seconds=uptime_seconds))
            print(f"System uptime: {uptime_str}")
        else:
            print("Unsupported OS for uptime display.")
    except Exception as e:
        print(f"Error ()
()
