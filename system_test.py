import random
import time

import requests

print("Setting things up...")
url = "http://localhost/api/search"
requests.post(url + "?query=Mustang ")

print("Searching existing terms...")
for attempt in range(5):
    start = time.time()
    res = requests.get(url + "?query=Mustang ")
    assert res.status_code == 200
    print("Existing | {} Time Taken :{}".format(attempt, time.time() - start))

print("Searching new terms...")
for attempt in range(5):
    start = time.time()
    query = str(random.randint(0, 100))
    res = requests.get(url + "?query='" + query+"'")
    assert res.status_code == 200
    print("Existing | {} Time Taken :{}".format(attempt, time.time() - start))
