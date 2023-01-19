from flask import Flask, render_template, request
from flask_restful import Api
import gymnasium as gym
# from flask_cors import CORS

from .api.reset import ResetResource
from .api.step import StepResource

app = Flask(__name__)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app, prefix= '/api')
env = gym.make("Blackjack-v1")
obs, info = env.reset(seed=42)

LOCAL = False
if LOCAL:
    prefix = "http://localhost:5222"
else:
    prefix = "https://bvme.azurewebsites.net"

api.add_resource(ResetResource, '/reset', resource_class_kwargs={ 'env': env })
api.add_resource(StepResource, '/step', resource_class_kwargs={ 'env': env })

@app.route('/')
def index():
    return render_template("index.html", content="Welcome to the Blackjack Game Server!")
