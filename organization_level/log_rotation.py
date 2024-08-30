import os
import shutil
from datetime import datetime

def rotate_logs(log_dir, archive_dir, max_size_mb):
    os.makedirs(archive_dir, exist_ok=True)

    for log_file in os.listdir(log_dir):
        file_path = os.path.join(log_dir, log_file)
        if os.path.isfile(file_path) and os.path.getsize(file_path) > max_size_mb * 1024 * 1024:
            archive_name = f"{log_file}_{datetime.now().strftime('%Y%m%d%H%M%S')}.log"
            shutil.move(file_path, os.path.join(archive_dir, archive_name))
            print(f"Rotated log file: {file_path} to {archive_name}")

log_directory = '/path/to/log/directory'
archive_directory = '/path/to/archive/directory'
max_file_size_mb = 5  # Maximum log file size in MB before rotation

rotate_logs(log_directory, archive_directory, max_file_size_mb)


''' It checks the size of each log file in the specified directory
  and moves it to an archive directory 
  if it exceeds the specified size.'''
