# Ultroid Extended - Web Server for Heroku
# Required to keep the app active and prevent dyno sleeping

import os
import time
import logging
import datetime
from flask import Flask, render_template, redirect, jsonify

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global variables for status tracking
START_TIME = time.time()
PING_COUNT = 0

@app.route('/')
def home():
    """Display the main status page"""
    return render_template('index.html')

@app.route('/ping')
def ping():
    """Simple ping endpoint for health checks"""
    global PING_COUNT
    PING_COUNT += 1
    return 'Pong! Ultroid is alive'

@app.route('/status')
def status():
    """Detailed status endpoint for monitoring"""
    global START_TIME, PING_COUNT
    
    uptime = time.time() - START_TIME
    uptime_str = str(datetime.timedelta(seconds=int(uptime)))
    
    # Get Heroku dyno info from environment variables
    dyno_type = os.environ.get('DYNO', 'unknown')
    app_name = os.environ.get('HEROKU_APP_NAME', 'ultroid-extended')
    
    status_data = {
        "status": "online",
        "uptime": uptime_str,
        "uptime_seconds": int(uptime),
        "ping_count": PING_COUNT,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "environment": {
            "dyno_type": dyno_type,
            "app_name": app_name,
            "python_version": os.environ.get('PYTHON_VERSION', 'unknown')
        }
    }
    
    return jsonify(status_data)

@app.route('/health')
def health_check():
    """Health check endpoint for Heroku"""
    return jsonify({"status": "healthy", "timestamp": time.time()})

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors gracefully"""
    return render_template('index.html'), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
