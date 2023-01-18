import requests
import json
import gymnasium as gym

# env = gym.make("Blackjack-v1")

# obs, info = env.reset(seed=43)
# print("reset obs: ", obs)
# terminated = False

# while terminated == False:
#     action = env.action_space.sample()
#     print("action: ", action)
#     obs, reward, terminated, truncated, info = env.step(action)
#     print("obs: ", obs, "reward: ", reward, "terminated: ", terminated, "truncated: ", truncated, "info: ", info)
    




# sendit = {
#     "name": "John Doe",
#     "email": "asdf@yml.com"
# }

sendit = {
    "seed": 44
}

LOCAL = False
if LOCAL:
    prefix = "http://localhost:5222"
else:
    prefix = "https://bvme.azurewebsites.net"
    

response = requests.request("POST",prefix + "/api/reset", 
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