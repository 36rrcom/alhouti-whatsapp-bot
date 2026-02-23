from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

def analyze(message):
    msg = message.lower()

    if "btc" in msg or "بيتكوين" in msg:
        return "📊 BTC حالياً حسب سكربت alhouti smart: راقب POWER و EXIT — السوق متقلب"

    if "شراء" in msg or "buy" in msg:
        return "🟢 لا تدخل إلا إذا POWER فوق 70% و EXIT أقل من 40%"

    if "بيع" in msg or "sell" in msg:
        return "🔴 البيع آمن فقط مع اتجاه الفريم الكبير + EXIT منخفض"

    if "خروج" in msg or "exit" in msg:
        return "⚠️ إذا EXIT تجاوز 60% اخرج فوراً حسب الاستراتيجية"

    return "🤖 أنا بوت سكربت alhouti smart — اسألني عن BTC، شراء، بيع، خروج"

@app.route("/whatsapp", methods=["POST"])
def reply():
    incoming = request.values.get("Body", "")
    response = MessagingResponse()
    msg = response.message()
    msg.body(analyze(incoming))
    return str(response)

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
from flask import Flask, request
from twilio.rest import Client
import os

app = Flask(__name__)

# بيانات Twilio من Environment Variables
ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
FROM_WHATSAPP = "whatsapp:+14155238886"  # Sandbox
TO_WHATSAPP = os.environ.get("YOUR_PHONE")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

@app.route("/alert", methods=["POST"])
def alert():
    data = request.json
    message = data.get("message", "No data")

    client.messages.create(
        body=message,
        from_=FROM_WHATSAPP,
        to=TO_WHATSAPP
    )

    return {"status": "sent"}
