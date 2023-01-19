from flask import Flask, render_template, request
from flask_restful import Api
import gymnasium as gym
import requests
from flask_cors import CORS
import json
import random

from .api.game import GameResource
from .api.reset import ResetResource
from .api.step import StepResource


app = Flask(__name__)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app, prefix= '/api')
env = gym.make("Blackjack-v1")

LOCAL = False
if LOCAL:
    prefix = "http://localhost:5222"
else:
    prefix = "https://bvme.azurewebsites.net"
    
api.add_resource(GameResource, '/game')
api.add_resource(ResetResource, '/reset', resource_class_kwargs={ 'env': env })
api.add_resource(StepResource, '/step', resource_class_kwargs={ 'env': env })

def fromReset(seed):
    sendit = {"seed": str(seed)}
    # response = requests.request("POST",prefix + "/api/reset", 
    #                             # json= json.dumps(sendit), 
    #                             json = sendit,
    #                             headers={"content-type": "application/json"})
    # print("response status code: ", response.status_code)
    # if response.status_code == 200:
    #     return response.json()
    return  {"player_sum": "1", 
                "dealer_sum": "1", 
                "usable_ace": str(False),
                "history": "not right", #+ str(response.status_code),
                "terminated": str(False),
                "reward": "0.0",
                "seed": str(seed)}

def fromStep(action, seed):
    sendit = {"action": str(action),
              "seed": str(seed)}
    print("sendit", sendit)
    response = requests.request("POST",prefix + "/api/step", 
                                json = sendit,
                                headers={"content-type": "application/json"})
    print("response", response.json())
    print("response status code: ", response.status_code)
    if response.status_code == 200:
        return response.json()
    return  {"player_sum": "1", 
                "dealer_sum": "1", 
                "usable_ace": str(False),
                "history": "not right step", #+ str(response.status_code),
                "terminated": str(False),
                "reward": "0.0",
                "seed": str(seed)}

def fromBonsai(seed):
    pass

# @app.route('/api/reset', methods=["POST"])
@app.route('/')
def index():
    return render_template("index.html", content="Welcome to the Blackjack Game2!")

@app.route("/play", methods=["POST", "GET"])
def play():
    data1 = {}
    print("in play")
    if request.method == "POST":
        if request.form["HitStick"] == "Hit":
            data1 = fromStep(1,request.form["seed"])
            return render_template("play.html",last_action="Hit", dealer_card=data1["dealer_sum"], player_card=data1["player_sum"], usable_ace=data1["usable_ace"], terminated=data1["terminated"], reward=data1["reward"], history=data1["history"], seed=data1["seed"])
        elif request.form["HitStick"] == "Stick":
            data1 = fromStep(0,request.form["seed"])
            return render_template("play.html",last_action="Stick", dealer_card=data1["dealer_sum"], player_card=data1["player_sum"], usable_ace=data1["usable_ace"], terminated=data1["terminated"], reward=data1["reward"], history=data1["history"], seed=data1["seed"])
        elif request.form["HitStick"] == "Reset":
            data1 = fromReset(request.form["seed"])
            return render_template("play.html",last_action="Reset", dealer_card=data1["dealer_sum"], player_card=data1["player_sum"], usable_ace=data1["usable_ace"], terminated=data1["terminated"], reward=data1["reward"], history=data1["history"],seed=data1["seed"])
        elif request.form["HitStick"] == "Bonsai":
            data1 = fromBonsai(request.form["seed"])
            return render_template("play.html",last_action="Bonsai", dealer_card=data1["dealer_sum"], player_card=data1["player_sum"], usable_ace=data1["usable_ace"], terminated=data1["terminated"], reward=data1["reward"], history=data1["history"],seed=data1["seed"])
    else:
        print("in main page reset")
        # return render_template("index.html", content="Welcome to the Blackjack Game3!")
        data1 = fromReset(seed=42)
        return render_template("play.html",last_action="Reset Start", dealer_card=data1["dealer_sum"], player_card=data1["player_sum"], usable_ace=data1["usable_ace"], terminated=data1["terminated"], reward=data1["reward"], history=data1["history"], seed=data1["seed"])

