import time
import requests

TOKEN = "8708625165:AAF63kNHGMeqNhdByOqEMGCwTA1q941_tAk"
URL = f"https://api.telegram.org/bot{TOKEN}/"

def get_updates(offset=None):
    params = {'timeout': 100, 'offset': offset}
    response = requests.get(URL + 'getUpdates', params=params)
    return response.json()

def send_message(chat_id, text):
    params = {'chat_id': chat_id, 'text': text}
    requests.post(URL + 'sendMessage', data=params)

def main():
    print("Bot is running successfully...")
    offset = None
    while True:
        updates = get_updates(offset)
        if "result" in updates:
            for update in updates["result"]:
                offset = update["update_id"] + 1
                if "message" in update and "text" in update["message"]:
                    chat_id = update["message"]["chat"]["id"]
                    user_text = update["message"]["text"]
                    
                    reply_text = f"Hello! I received your message: {user_text}"
                    send_message(chat_id, reply_text)
        time.sleep(1)

if __name__ == '__main__':
    main()
  
