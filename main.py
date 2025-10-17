from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8331188037:AAHczNrYr_JyADC80Aj2BuOrr47wAcYFY24"  
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


if __name__ == '__main__':
  
    app.run(host='0.0.0.0', port=5000)
