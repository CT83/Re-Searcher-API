import random
import time

import requests

print("Setting things up...")
url = "http://localhost/api/search"
requests.post(url, json={"query": "Pink Car", "engine": "bing"})

print("Searching existing terms...")
for attempt in range(5):
    start = time.time()
    payload = {"query": "Pink Car", "engine": "bing"}
    res = requests.post(url, json=payload)
    assert res.status_code == 200
    print("Existing | {} Time Taken :{}".format(attempt, time.time() - start))

print("Searching new terms...")
for attempt in range(5):
    start = time.time()
    payload = {"query": str(random.randint(0, 9999)), "engine": "bing"}
    res = requests.post(url, json=payload)
    assert res.status_code == 200
    print("Existing | {} Time Taken :{}".format(attempt, time.time() - start))
