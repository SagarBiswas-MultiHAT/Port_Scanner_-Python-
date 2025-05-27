from flask import Flask, render_template, request, jsonify
import socket
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import os

app = Flask(__name__)

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
            return port, True
    except:
        return port, False

def scan_ports(ip, ports):
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda p: scan_port(ip, p), ports)
        for port, is_open in results:
            if is_open:
                open_ports.append(port)
    return open_ports

def validate_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    target_ip = request.json.get('ip')
    port_range = request.json.get('port_range', '1-1000')

    if not validate_ip(target_ip):
        return jsonify({"error": "Invalid IP address."}), 400

    try:
        start_port, end_port = map(int, port_range.split('-'))
        ports = range(start_port, end_port + 1)
    except ValueError:
        return jsonify({"error": "Invalid port range."}), 400

    start_time = datetime.now()
    open_ports = scan_ports(target_ip, ports)
    duration = (datetime.now() - start_time).total_seconds()

    # Save results to a log file
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"scan_{target_ip}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    with open(log_file, 'w') as f:
        f.write(f"Scan results for {target_ip}\n")
        f.write(f"Port range: {port_range}\n")
        f.write(f"Open ports: {', '.join(map(str, open_ports)) if open_ports else 'None'}\n")
        f.write(f"Duration: {duration} seconds\n")

    return jsonify({"open_ports": open_ports, "duration": duration, "log_file": log_file})

if __name__ == "__main__":
    app.run(debug=True)
