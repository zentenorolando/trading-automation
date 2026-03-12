from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/tradingview", methods=["POST"])
def tradingview():
    data = request.json
    print("Received alert:", data)
    return "ok"

app.run(host="0.0.0.0", port=8000)
