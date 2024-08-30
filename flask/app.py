from flask import Flask, render_template
import shutil

app = Flask(__name__)

def check_disk_usage(path, threshold):
    total, used, free = shutil.disk_usage(path)
    usage_percent = (used / total) * 100
    
    if usage_percent > threshold:
        return f"Warning: Disk usage has exceeded {threshold}% at {path}! Current usage: {usage_percent:.2f}%"
    else:
        return f"Disk usage at {path}: {usage_percent:.2f}%"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_usage')
def check_usage():
    monitor_path = '/'
    usage_threshold = 70  # Set the threshold percentage
    result = check_disk_usage(monitor_path, usage_threshold)
    return result

if __name__ == '__main__':
    app.run(debug=True)
