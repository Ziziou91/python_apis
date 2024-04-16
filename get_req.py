import requests

# http://postcodes.io/

postcodes_req = requests.get("https://api.postcodes.io/postcodes/SK30DL")
# print(postcodes_req)
# print(postcodes_req.status_code)
# print(postcodes_req.headers)
# Note that the type of .content is 'bytes'
# print(postcodes_req.content)
# Returns a dictionary
print(postcodes_req.json())

data_dict = postcodes_req.json()["result"]
print(data_dict)
