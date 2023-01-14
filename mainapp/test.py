import requests
import json

# sendit = {
#     "name": "John Doe",
#     "email": "asdf@yml.com"
# }

sendit = {
    "seed": 44
}

response = requests.request("POST","http://localhost:5222/api/reset", 
                            json= json.dumps(sendit), 
                            headers={"content-type": "application/json"})
print("response: ", response.json())
full = response.json()
print("full: ", full["player_sum"])

# POST http://localhost:5000/api/reset HTTP/1.1
# content-type: application/json

# {
#     "seed": "42"
# }

# POST http://localhost:5600/api/profiles HTTP/1.1
# content-type: application/json

# {
#     "name": "John Doe",
#     "email": "asdf@yml.com"
# }