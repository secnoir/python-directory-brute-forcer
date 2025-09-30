import requests
import threading
from queue import Queue

target = "http://testphp.vulnweb.com"
wordlist_file = "/usr/share/seclists/Discovery/Web-Content/common.txt"

with open(wordlist_file, "r") as f:
    words = f.read().splitlines()

q = Queue()
for word in words:
    q.put(word)

def worker():
    while not q.empty():
        word = q.get()
        url = f"{target}/{word}"
        try:
            r = requests.get(url, timeout=2)
            if r.status_code != 404:
                print(f"[{r.status_code}] {url}")
        except requests.exceptions.RequestException:
            pass
        q.task_done()

# spawn threads
for _ in range(20):  # 20 threads
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

q.join()
