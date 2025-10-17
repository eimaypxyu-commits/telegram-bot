from flask import Flask, request
import requests, os

app = Flask(__name__)

# Environment Variable Key ကို BOT_TOKEN လို့ သုံးပါမည်
TOKEN = os.getenv("BOT_TOKEN")  
URL = f"https://api.telegram.org/bot{TOKEN}"

@app.route('/')
def home():
    return "🤖 Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if 'message' in data and 'text' in data['message']:
        chat_id = data['message']['chat']['id']
        text = data['message']['text']

        reply = f"👋 Channel_J_Movies က ကြိုဆိုပါတယ်:\n\n{text}"
        requests.post(f"{URL}/sendMessage", json={'chat_id': chat_id, 'text': reply})

    return '', 200

# Production (Render) မှာ Gunicorn ကို အသုံးပြုပါမည်။
# Gunicorn သည် Flask app object ကို အလိုအလျောက် ရှာဖွေပြီး Run ပါမည်။
# Local run အတွက် လိုအပ်သော if __name__ == '__main__': အပိုင်းကို ချန်လှပ်ထားပါသည်။
