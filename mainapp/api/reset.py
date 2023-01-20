import json
from flask import request
from flask_restful import Resource
import gymnasium as gym
import warnings

class ResetResource(Resource):

    def __init__(self, **kwargs):
        self.env = kwargs["env"]
    # list of players from session?  Dictionary with env pointer?
    
    def get(self):
        print("in get in reset")
        return {"dealer_card": "4", "player_card": "5"}
    
    def post(self):
        warnings.warn("in full reset")
        try:
                # data = request.get_json()?
            warnings.warn("request type" + str(type(request.json)))
            # data = json.loads(request.json)
            data = json.loads(request.json) #(depending where)

            if "seed" in data.keys():
                seed = int(data["seed"])
            else:
                seed = 42
            warnings.warn("request seed" + str(seed))
            obs, info = self.env.reset(seed=seed)
            print("reset obs: ", obs)
            hist = f"Deal, Player Total: {obs[0]}, Usable Ace: {obs[2]}"
            print("hist: ", hist)
            return {"player_sum": str(obs[0]), 
                    "dealer_sum": str(obs[1]), 
                    "usable_ace": str(obs[2]),
                    "terminated": str(False),
                    "reward": "0.0",
                    "history": hist,
                    "seed": str(seed)}
        except:
            warnings.warn("in except full reset")
            return  {"player_sum": "1", 
                "dealer_sum": "1", 
                "usable_ace": str(False),
                "history": "not right full reset",
                "terminated": str(False),
                "reward": "0.0",
                "seed": str(seed)}
        