import requests
import json

# http://postcodes.io/

json_body = json.dumps({"postcodes": ["SK3 0DL", "M4 6FR", "EX165BL"]})
headers = {"Content-Type": "application/json"}

# post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)
# print(post_multi_req.json())

# data -> accepts a string (so we had to use json.dumps first)
# json -> accepts a python dictionary
post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, json={"postcodes": ["SK3 0DL", "M4 6FR", "EX165BL"]})
print(post_multi_req.json())
