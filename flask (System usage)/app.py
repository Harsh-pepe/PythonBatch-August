from flask import Flask, render_template
import shutil
import psutil  # Import the psutil library

app = Flask(__name__)

# Function to check disk usage
def check_disk_usage(path, threshold):
    total, used, free = shutil.disk_usage(path)
    usage_percent = (used / total) * 100
    
    if usage_percent > threshold:
        return f"Warning: Disk usage has exceeded {threshold}% at {path}! Current usage: {usage_percent:.2f}%"
    else:
        return f"Disk usage at {path}: {usage_percent:.2f}%"

# Function to check memory usage
def check_memory_usage():
    memory = psutil.virtual_memory()
    usage_percent = memory.percent
    return f"Memory Usage: {usage_percent:.2f}%"

# Function to check CPU usage
def check_cpu_usage():
    usage_percent = psutil.cpu_percent(interval=1)
    return f"CPU Usage: {usage_percent:.2f}%"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_usage')
def check_usage():
    monitor_path = '/'
    usage_threshold = 80  # Set the threshold percentage
    disk_result = check_disk_usage(monitor_path, usage_threshold)
    memory_result = check_memory_usage()
    cpu_result = check_cpu_usage()

    # Combine all results into a single response
    result = f"{disk_result}<br>{memory_result}<br>{cpu_result}"
    return result

if __name__ == '__main__':
    app.run(debug=True)
