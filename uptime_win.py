import subprocess
import platform
import re
from datetime import datetime

def get_system_uptime():
    os_type = platform.system()

    if os_type == 'Darwin':  # macOS
        result = subprocess.run(['sysctl', '-n', 'kern.boottime'], stdout=subprocess.PIPE)
        boot_time_str = result.stdout.decode().strip()

        # Extract the boot time in seconds using a regular expression
        boot_time_match = re.search(r'{ sec = (\d+),', boot_time_str)
        if boot_time_match:
            boot_time_seconds = int(boot_time_match.group(1))
        else:
            print("Could not determine boot time on macOS.")
            return

        # Get the current time in seconds since epoch
        current_time_seconds = int(subprocess.run(['date', '+%s'], stdout=subprocess.PIPE).stdout.decode().strip())

        # Calculate the uptime in seconds
        uptime_seconds = current_time_seconds - boot_time_seconds

    elif os_type == 'Windows':  # Windows
        # Run the 'wmic os get lastbootuptime' command to get the last boot time
        result = subprocess.run(['wmic', 'os', 'get', 'lastbootuptime'], stdout=subprocess.PIPE)
        boot_time_str = result.stdout.decode().strip().split('\n')[1]

        # Parse the WMIC output to get boot time
        boot_time = datetime.strptime(boot_time_str.split('.')[0], '%Y%m%d%H%M%S')

        # Calculate uptime in seconds
        current_time = datetime.now()
        uptime_seconds = (current_time - boot_time).total_seconds()

    else:
        print(f"Unsupported operating system: {os_type}")
        return

    # Convert uptime to hours
    uptime_hours = uptime_seconds / 3600
    print(f"System Uptime: {uptime_hours:.2f} hours")

get_system_uptime()
