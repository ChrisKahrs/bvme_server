from flask import Flask, render_template, request
from flask_restful import Api

from .api.game import GameResource

app = Flask(__name__)
api = Api(app, prefix= '/api')

api.add_resource(GameResource, '/game')

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
        return render_template("play.html", dealer_card="4", player_card="5")

