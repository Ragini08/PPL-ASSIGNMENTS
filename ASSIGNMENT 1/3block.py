# WEBSITE BLOCKER

import time
from datetime import datetime as dt

# Path to the host file, redirect to local host, list of websits to block
host_path = "/etc/hosts"
redirect: str = "127.0.0.1"
website_list = ["www.facebook.com"]

# Condition
while True:
    # Check for the current time
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,
                                                                          17):
        print("Working hours..")
        file = open(host_path, "r+")
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                file.write(redirect + " " + website + "\n")
    else:
        print("Fun time...")
        file = open(host_path, 'r+')
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
            file.truncate()
    time.sleep(2)


