from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "name": "Jarvis",
        "commander": "Preet"
    })

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    user_message = data.get("message", "")

    reply = f"Jarvis received: {user_message}"

    return jsonify({
        "reply": reply,
        "speaker": "Jarvis"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
