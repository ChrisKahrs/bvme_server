import json
from flask import request, g
from flask_restful import Resource
import gymnasium as gym

class ResetResource(Resource):

    def __init__(self, **kwargs):
        self.env = kwargs["env"]
    # list of players from session?  Dictionary with env pointer?
    
    def get(self):
        return {"dealer_card": "4", "player_card": "5"}
    
    def post(self):
        print("request", request.json)
        data = json.loads(request.json)

        if "seed" in data.keys():
            seed = int(data["seed"])
        else:
            seed = 42
        obs, info = self.env.reset(seed=seed)
        print("reset obs: ", obs)
        return { "player_sum": str(obs[0]) }
        