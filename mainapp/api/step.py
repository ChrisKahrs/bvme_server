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
        print("in post")
        data = json.loads(request.json)
        print("data type: ", type(data))
        action = data["action"]
        print("action: ", action)
        obs, reward, terminated, truncated, info = self.env.step(int(data["action"]))
        if action == "1":
            hist = f"Hit, Player Total: {obs[0]}, Usable Ace: {obs[2]}\n"
        else:
            hist = f"Stick, Player Total: {obs[0]}, Usable Ace: {obs[2]}\n"
        if reward > 0:
            hist += f"WINNER: {reward}"
        elif reward < 0:
            hist += f"LOSER: {reward}"
        print("obs: ", obs, "reward: ", reward, "terminated: ", terminated, "truncated: ", truncated, "info: ", info)
        return {"player_sum": str(obs[0]), 
                "dealer_sum": str(obs[1]), 
                "usable_ace": str(obs[2]),
                "terminated": str(terminated),
                "reward": reward, 
                "history": hist,
                "seed": data["seed"]}