# Port Scanner (Python)

![](https://imgur.com/LX7MfC8.png)

## Description
This project is a Python-based port scanner designed for educational purposes. It allows users to scan open TCP ports on a target machine. The tool can be used via a command-line interface or a web-based GUI built with Flask.

## Features
- Scans the top 1000 TCP ports by default.
- Allows custom port range scanning.
- Logs scan results to a file for later analysis.
- Displays scan duration and performance metrics.
- Web-based GUI for ease of use.
- Input validation and error handling.

## Installation
1. Clone the repository or download the project files.
2. Navigate to the `Port_Scanner_(Python)` directory.
3. Install the required dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Usage

### Command-Line Interface
1. Run the `port_scanner.py` script:
   ```powershell
   python port_scanner.py
   ```
2. Enter the target IP address when prompted.

### Web-Based GUI
1. Run the Flask application:
   ```powershell
   python app.py
   ```
2. Open your browser and navigate to `http://127.0.0.1:5000`.
3. Enter the target IP address and optional port range, then click "Scan".

## Logs
Scan results are saved in the `logs` folder within the `Port_Scanner_(Python)` directory. Each log file is named with the target IP and timestamp.

## Example Target IPs
Refer to the `example.txt` file for sample target IPs to use for testing.

## Disclaimer
This tool is intended for educational purposes only. Ensure you have proper authorization before scanning any network or device. Unauthorized scanning is illegal and unethical.

## Concepts Learned
- Networking basics
- TCP/IP
- Ethical scanning principles

