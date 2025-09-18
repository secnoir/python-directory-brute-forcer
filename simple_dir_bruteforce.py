# Simple Directory Brute Forcer
# Author: Irfan
# Description: Sends HTTP requests for a list of paths and reports which ones exist.



import requests

target = "http://youtube.com"
wordlist = ["admin", "user", "test"]
for word in wordlist:
    url = f"{target}/{word}/"
    try:
        response = requests.get(url, timeout=2)
        if response.status_code == 200:
            print(f"Found: {url}")
        elif response.status_code == 403:
            print(f"Forbidden: {url}")
    except requests.exceptions.Request.Exception:
            pass



