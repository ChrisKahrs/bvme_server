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
    sendit = {"seed": seed}
    response = requests.request("POST","http://localhost:5222/api/reset", 
                                json= json.dumps(sendit), 
                                headers={"content-type": "application/json"})
    return response.json()

def fromStep(action, seed):
    sendit = {"action": str(action),
              "seed": str(seed)}
    print("sendit", sendit)
    response = requests.request("POST","http://localhost:5222/api/step", 
                                json= json.dumps(sendit), 
                                headers={"content-type": "application/json"})
    print("response", response.json())
    return response.json()

def fromBonsai(seed):
    pass

@app.route('/api/reset', methods=["POST"])
@app.route('/')
def index():
    return render_template("index.html", content="Welcome to the Blackjack Game!")

@app.route("/play", methods=["POST", "GET"])
def play():
    data1 = {}
    if request.method == "POST":
        if request.form["HitStick"] == "Hit":
            data1 = fromStep(1,request.form["seed"])
            return render_template("play.html",last_action="Hit", dealer_card=data1["dealer_sum"], player_card=data1["player_sum"], usable_ace=data1["usable_ace"], terminated=data1["terminated"], reward=data1["reward"], history=data1["history"], seed=data1["seed"])
        elif request.form["HitStick"] == "Stick":
            data1 = fromStep(0,request.form["seed"])
            return render_template("play.html",last_action="Stick", dealer_card=data1["dealer_sum"], player_card=data1["player_sum"], usable_ace=data1["usable_ace"], terminated=data1["terminated"], reward=data1["reward"], history=data1["history"], seed=data1["seed"])
        elif request.form["HitStick"] == "Reset":
            data1 = fromReset(request.form["seed"])
            return render_template("play.html",last_action="Reset", dealer_card=data1["dealer_sum"], player_card=data1["player_sum"], usable_ace=data1["usable_ace"], history=data1["history"],seed=data1["seed"])
        elif request.form["HitStick"] == "Bonsai":
            data1 = fromBonsai(request.form["seed"])
            return render_template("play.html",last_action="Bonsai", dealer_card=data1["dealer_sum"], player_card=data1["player_sum"], usable_ace=data1["usable_ace"], history=data1["history"],seed=data1["seed"])
    else:
        data1 = fromReset(seed=42)
        return render_template("play.html",last_action="Reset Start", dealer_card=data1["dealer_sum"], player_card=data1["player_sum"], usable_ace=data1["usable_ace"], history=data1["history"], seed=data1["seed"])

