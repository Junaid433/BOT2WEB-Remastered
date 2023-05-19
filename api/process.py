from flask import Blueprint, request
import requests
import threading 

process_bp = Blueprint('process_bp', __name__)
lock = threading.Lock()

@process_bp.route('/process')
def process():
    with lock:
        if request.args.get('gate') == 'vbv':
            return requests.get('http://localhost:5000/vbv?cc='+request.args.get('cc')).text
        elif request.args.get('gate') == 'auth':
            return requests.get('http://localhost:5000/chk?cc='+request.args.get('cc')).text