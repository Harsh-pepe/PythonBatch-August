import os
import shutil

def check_disk_usage(path, threshold):
    total, used, free = shutil.disk_usage(path)
    usage_percent = (used / total) * 100
    
    print(f"Disk usage at {path}: {usage_percent:.2f}%")
    
    if usage_percent > threshold:
        print(f"Warning: Disk usage has exceeded {threshold}% at {path}")

monitor_path = '/Users/harsh/Music/Python Projects August'
usage_threshold = 70  # Set the threshold percentage

check_disk_usage(monitor_path, usage_threshold)
