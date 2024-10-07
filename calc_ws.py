# A lib FLASK cria um Web Service (WS)
# localhost porta padão 5000
# pip3 install Flask

from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    now = str(datetime.datetime())
    return f"<p>Hello, FIAP! {now}</p>"

@app.route("add/<a>/<b>")
def add(a, b):
    return str(float(a) + float(b))