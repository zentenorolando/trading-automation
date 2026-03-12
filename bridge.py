from flask import Flask, request

app = Flask(__name__)

@app.route('/tradingview', methods=['POST'])
def tradingview():

    data = request.json
    print("Received alert:", data)

    return {"status": "ok"}

@app.route("/")
def home():
    return "Trading bridge running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
