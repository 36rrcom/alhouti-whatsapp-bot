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

if __name__ == "__main__":
    app.run()
