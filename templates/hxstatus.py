#!/usr/bin/env python3
import subprocess
import sys
import time
import json
from datetime import datetime

print(json.dumps({"version": 1}))
print("[")
print("[],")
sys.stdout.flush()

def get_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def is_charging():
    try:
        output = subprocess.check_output(
            ["cat", "/sys/class/power_supply/BAT0/status"],
            text=True,
        ).strip()
        return output == "Charging"
    except:
        return False

def get_battery():
    try:
        output = subprocess.check_output(
            ["cat", "/sys/class/power_supply/BAT0/capacity"],
            text=True,
        ).strip()
        if is_charging():
            return f"<span foreground='#7CFC00' size='x-large'>{output}%</span>"
        elif int(output) < 30:
            return f"<span foreground='red' size='x-large' weight='bold'>{output}%</span>"
        else:
            return str(output) + "%"
    except Exception:
        return "N/A"

while True:
    status = [
        {
            "full_text": f"{get_battery()} | {get_datetime()}",
            "markup": "pango",
        }
    ]

    print(json.dumps(status) + ",")
    sys.stdout.flush()
    time.sleep(1)
