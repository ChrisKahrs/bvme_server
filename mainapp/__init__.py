from flask import Flask, render_template, request
from flask_restful import Api
import gymnasium as gym
import requests 
import json


from .api.game import GameResource
from .api.reset import ResetResource
from .api.step import StepResource

app = Flask(__name__)
api = Api(app, prefix= '/api')
env = gym.make("Blackjack-v1")

api.add_resource(GameResource, '/game')
api.add_resource(ResetResource, '/reset', resource_class_kwargs={ 'env': env })
api.add_resource(StepResource, '/step', resource_class_kwargs={ 'env': env })

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
    else:
        response = requests.post("http://localhost:5000/api/reset", json= {"seed": 42})
        print("response: ", response)
        prediction = response.json()
        print("prediction: ", prediction)
        return render_template("play.html", dealer_card="4", player_card=prediction["player_sum"])

