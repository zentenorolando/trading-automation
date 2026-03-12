from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/tradingview", methods=["POST"])
def tradingview():

    data = request.json

    symbol = data.get("symbol")
    action = data.get("action")
    size = data.get("size")

    print("----- ALERT RECEIVED -----")
    print("Symbol:", symbol)
    print("Action:", action)
    print("Size:", size)

    # Placeholder for trade execution
    if action == "buy":
        print("Executing BUY order")

    elif action == "sell":
        print("Executing SELL order")

    return "ok"

app.run(host="0.0.0.0", port=8000)
