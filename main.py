from flask import Flask, request
import requests
import os

TOKEN = os.getenv("BOT_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}"

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()

    if data and "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        requests.post(f"{URL}/sendMessage", json={
            "chat_id": chat_id,
            "text": f"🤖 Bot nhận được: {text}"
        })

    return "ok"

@app.route("/")
def home():
    return "Bot Telegram đang chạy!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
