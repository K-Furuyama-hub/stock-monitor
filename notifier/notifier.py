from flask import Flask, request
import requests

DISCORD_WEBHOOK_URL = "YOUR_WEBHOOK_URL"

app = Flask(__name__)

@app.route("/alert",methods=["POST"])
def alert():
    data = request.json # 受け取ったJSONを読む

    # アラートが複数来ることがあるのでループ
    for a in data.get("alerts",[]):
        name = a["labels"].get("alertname","不明")
        status = a["status"] # firing or resolved
        msg = f"【株価アラート】{name} - {status}"

        # DiscordへPOST
        requests.post(DISCORD_WEBHOOK_URL, json={"content": msg})

    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)