import json
from flask import request
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
        # data = request.json #(depending where)

        if "seed" in data.keys():
            seed = int(data["seed"])
        else:
            seed = 42
        obs, info = self.env.reset(seed=seed)
        print("reset obs: ", obs)
        hist = f"Deal, Player Total: {obs[0]}, Usable Ace: {obs[2]}"
        print("hist: ", hist)
        return {"player_sum": str(obs[0]), 
                "dealer_sum": str(obs[1]), 
                "usable_ace": str(obs[2]),
                "history": hist,
                "seed": str(seed)}
        