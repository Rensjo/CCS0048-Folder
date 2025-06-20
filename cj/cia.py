import subprocess
import re

LOG_FILE = "/var/log/suricata/fast.log"  # Adjust if using Snort

def block_attacker(ip):
    subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])
    print(f"Blocked IP: {ip}")

def monitor_logs():
    with open(LOG_FILE, "r") as file:
        file.seek(0, 2)  # Go to end of file

        while True:
            line = file.readline().strip()
            if not line:
                time.sleep(1)
                continue

            if "NMAP" in line:
                ip_match = re.search(r'(\d{1,3}\.){3}\d{1,3}', line)
                if ip_match:
                    ip = ip_match.group()
                    block_attacker(ip)

if __name__ == "__main__":
    print("Starting log monitor. Press Ctrl+C to stop.")
    monitor_logs()
