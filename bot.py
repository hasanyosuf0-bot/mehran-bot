import telebot
import requests

# التوكن الخاص بالبوت الذي أرسلته
TELEGRAM_TOKEN = '8985832742:AAGpFqyjxpkcJCZ3-GnHGDe_3DLdJ6y0ddM'
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# مفتاح Gemini API (يمكنك استبداله بمفتاحك الخاص من Google AI Studio ليعمل الذكاء الاصطناعي)
GEMINI_API_KEY = 'YOUR_GEMINI_API_KEY'

def get_ai_response(user_message):
    """وظيفة لإرسال الرسالة إلى الذكاء الاصطناعي وجلب الرد"""
    url = f"https://googleapis.com{GEMINI_API_KEY}"
    headers = {'Content-Type': 'application/json'}
    
    # توجيه الذكاء الاصطناعي ليتحدث كخبير أمن سيبراني وبرمجة باللغة العربية
    system_instruction = "أنت خبير في البرمجة والأمن السيبراني والهاكر الأخلاقي. أجب دائماً باللغة العربية بأسلوب ذكي، مبسط، ومحترف."
    
    payload = {
        "contents": [{"parts": [{"text": user_message}]}],
        "systemInstruction": {"parts": [{"text": system_instruction}]}
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            result = response.json()
            return result['candidates'][0]['content']['parts'][0]['text']
        else:
            return "عذراً، أواجه مشكلة في الاتصال بعقلي الاصطناعي حالياً. تأكد من إعداد مفتاح API بشكل صحيح."
    except Exception as e:
        return "حدث خطأ أثناء معالجة الطلب."

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! أنا مساعدك الذكي المتخصص في البرمجة، الأمن السيبراني، والهاكر الأخلاقي. كيف يمكنني مساعدتك اليوم؟ اسألني أي شيء!")

@bot.message_handler(func=lambda message: True)
def chat_with_ai(message):
    # إظهار أن البوت "يكتب الآن..." لجعل التجربة طبيعية
    bot.send_chat_action(message.chat.id, 'typing')
    
    # جلب رد الذكاء الاصطناعي
    ai_reply = get_ai_response(message.text)
    
    # إرسال الرد للمستخدم
    bot.reply_to(message, ai_reply)

if __name__ == '__main__':
    print("البوت الذكي يعمل الآن...")
    bot.polling(none_stop=True)
