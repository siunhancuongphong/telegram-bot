from flask import Flask, request
import requests
import os

# KHỞI TẠO FLASK APP (BẮT BUỘC PHẢI Ở TRÊN)
app = Flask(__name__)

TOKEN = os.getenv("BOT_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()

    if not data or "message" not in data:
        return "ok"

    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")

    if text == "/start":
        reply = "👋 Chào bạn!\nBot đã hoạt động thành công 🎉"
    else:
        reply = f"🤖 Bot nhận được: {text}"

    requests.post(f"{URL}/sendMessage", json={
        "chat_id": chat_id,
        "text": reply
    })

    return "ok"

@app.route("/")
def home():
    return "Bot Telegram đang chạy!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
