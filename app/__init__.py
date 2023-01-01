from flask import Flask, render_template

from .profiles import profiles_blueprint

app = Flask(__name__)

app.register_blueprint(profiles_blueprint)

@app.route('/')
def index():
    return render_template('index.html')




