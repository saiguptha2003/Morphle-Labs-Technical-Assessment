from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "V D Panduranga Sai Guptha"
    username = os.getenv('USER') or os.getenv('LOGNAME') or 'unknown_user'
    serverTime = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time() + 19800))
    topOutput = subprocess.getoutput("top -bn1 | head -n 10")
    return f"""
    <html>
        <head><title>System Info</title></head>
        <body>
            <h1>System Information</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {serverTime}</p>
            <h2>Top Output</h2>
            <pre>{topOutput}</pre>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
