from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    my_ip = requests.get("https://www.ifconfig.me/")
    return f"Hello from {my_ip.text}"