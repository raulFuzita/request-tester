from flask import request, jsonify
from datetime import datetime, timedelta
from ...exception.httprequest.http_error import HTTPError
from dotenv import load_dotenv
import os

load_dotenv()

# Get the limit requests and time window from the environment variables
SERVER_LIMIT_REQUESTS = os.getenv('SERVER_LIMIT_REQUESTS')
SERVER_LIMIT_TIME = os.getenv('SERVER_LIMIT_TIME')

if SERVER_LIMIT_REQUESTS and SERVER_LIMIT_TIME:
    SERVER_LIMIT_REQUESTS = int(SERVER_LIMIT_REQUESTS)
    SERVER_LIMIT_TIME = int(SERVER_LIMIT_TIME)
    time_window = timedelta(minutes=SERVER_LIMIT_TIME)
else:
    SERVER_LIMIT_REQUESTS = None
    SERVER_LIMIT_TIME = None

ip_request_count = {}

def default_limit_ip_requests():
    limit_ip_requests(True)

def limit_ip_requests(json_response=None):
    global ip_request_count
    
    if SERVER_LIMIT_REQUESTS and SERVER_LIMIT_TIME:
        current_time = datetime.utcnow()
        ip = request.remote_addr
        
        # Clean up old entries
        for key in list(ip_request_count.keys()):
            if current_time - ip_request_count[key]['first_request_time'] > time_window:
                del ip_request_count[key]
        
        # Check the request count for the current IP
        if ip in ip_request_count:
            ip_request_count[ip]['count'] += 1
            if ip_request_count[ip]['count'] > SERVER_LIMIT_REQUESTS:
                if json_response:
                    return jsonify(message="Too many requests"), 429
                else:
                    raise HTTPError("Too many requests", 429)
        else:
            ip_request_count[ip] = {'count': 1, 'first_request_time': current_time}
