### old use starup2.py method
# 
# 
from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", content="Welcome to the Blackjack Game1!")

@app.route("/play", methods=["POST", "GET"])
def play():
    if request.method == "POST":
        if request.form["HitStick"] == "Hit":
            return render_template("index.html", content="Hit")
        elif request.form["HitStick"] == "Stick":
            return render_template("index.html", content="Stick")
    else:
        return render_template("play.html", dealer_card="4", player_card="5")

if __name__ == "__main__":
    app.run(debug=True)
    