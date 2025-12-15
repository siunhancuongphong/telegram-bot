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
