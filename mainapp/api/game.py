import json
from flask import request
from flask_restful import Resource
import requests


def fromReset():
    sendit = {
        "seed": 44
    }
    response = requests.request("POST","http://localhost:5222/api/reset", 
                                json= json.dumps(sendit), 
                                headers={"content-type": "application/json"})
    print("response: ", response)
    data = response.json()
    print("data: ", data["player_sum"])
    return data

class GameResource(Resource):
    def get(self):
        return {"dealer_card": "4", "player_card": "5"}
    
    def post(self):
        print("request", request)
        data = json.loads(request.data)
        print("data", data)
        if data["HitStick"] == "Hit":
            return {"content": "Hit"}
        elif data["HitStick"] == "Stick":
            return {"content": "Stick"}
        elif data["HitStick"] == "Reset":
            return fromReset()