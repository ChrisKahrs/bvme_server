from flask import Flask, render_template, request
from flask_restful import Api
import gymnasium as gym
import requests 
import json
import random


from .api.game import GameResource
from .api.reset import ResetResource
from .api.step import StepResource

app = Flask(__name__)
api = Api(app, prefix= '/api')
env = gym.make("Blackjack-v1")

api.add_resource(GameResource, '/game')
api.add_resource(ResetResource, '/reset', resource_class_kwargs={ 'env': env })
api.add_resource(StepResource, '/step', resource_class_kwargs={ 'env': env })

def fromReset(seed):
    sendit = {
        "seed": seed
    }
    response = requests.request("POST","http://localhost:5222/api/reset", 
                                json= json.dumps(sendit), 
                                headers={"content-type": "application/json"})
    print("response: ", response)
    data = response.json()
    print("ace: ", data["usable_ace"])
    return data

@app.route('/api/reset', methods=["POST"])
@app.route('/')
def index():
    return render_template("index.html", content="Welcome to the Blackjack Game!")

@app.route("/play", methods=["POST", "GET"])
def play():
    if request.method == "POST":
        if request.form["HitStick"] == "Hit":
            return render_template("index.html", content="Hit")
        elif request.form["HitStick"] == "Stick":
            return render_template("index.html", content="Stick")
        elif request.form["HitStick"] == "Reset":
            data1 = fromReset(request.form["seed"])
            return  render_template("play.html", dealer_card=data1["dealer_sum"], player_card=data1["player_sum"], usable_ace=data1["usable_ace"], seed=data1["seed"])
    else:
        #reset and give cards
        data1 = fromReset(seed=42)
        return  render_template("play.html", dealer_card=data1["dealer_sum"], player_card=data1["player_sum"], usable_ace=data1["usable_ace"], seed=data1["seed"])

