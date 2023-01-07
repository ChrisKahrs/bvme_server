import json
from flask import request
from flask_restful import Resource

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