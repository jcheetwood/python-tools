"""
Replace URL TO SPAM with url and port of your choice.

Can be used to test request counts and high load on web servers.
"""

import subprocess
import os


curl_cmd = ["curl", "-i", "URL TO SPAM"]
processes = set()
max_processes = 100

for i in range(0,1500000):
    processes.add(subprocess.Popen(curl_cmd))
    print(i)
    if len(processes) >= max_processes:
        os.wait()
        processes.difference_update([
            p for p in processes if p.poll() is not None])









