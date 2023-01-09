import json
from flask import request
from flask_restful import Resource
import gymnasium as gym

class StepResource(Resource):
    
    def __init__(self, **kwargs):
        self.env = kwargs["env"]
        
    def get(self):
        return {"dealer_card": "4", "player_card": "5"}
    
    def post(self):
        print("request", request)
        data = json.loads(request.data)
        # print("data", data)
        # if data["HitStick"] == "Hit":
        #     return {"content": "Hit"}
        # elif data["HitStick"] == "Stick":
        #     return {"content": "Stick"}
        obs, reward, terminated, truncated, info = self.env.step(int(data["action"]))
        print("obs: ", obs, "reward: ", reward, "terminated: ", terminated, "truncated: ", truncated, "info: ", info)