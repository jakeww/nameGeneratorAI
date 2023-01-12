import requests
import json
import time

url = "https://data.oregon.gov/resource/tckn-sxa6.json?$limit=5000"
offset = 0

with open("rawNameData.txt", "a") as f: # open file in append mode
    while True:
        response = requests.get(url + "&$offset=" + str(offset))
        data = json.loads(response.text)
        if not data:
            break
        for item in data:
            f.write(item["business_name"] + "\n")
        offset += 5000
        time.sleep(2) # wait for 2 seconds
