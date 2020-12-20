import requests
import json
api_url = "http://numbersapi.com/"
with open("dataset_24476_3.txt", "r") as inf, open("result.txt", "w") as ouf:
    numbers = [int(x) for x in inf.read().split()]
    for number in numbers:
        res = requests.get(f"{api_url}{number}/math?json=true")
        data = res.json()
        if data["found"]:
            ouf.write("Interesting\n")
        else:
            ouf.write("Boring\n")
