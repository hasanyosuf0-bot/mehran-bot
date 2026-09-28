import telebot
import requests

# التوكن الخاص بك
TOKEN = '8985832742:AAFZd44EbyEUCWrhUS2OXFkrNMOJqflALwY'
bot = telebot.TeleBot(TOKEN)

print("🚀 البوت المطور بالذكاء الاصطناعي بدأ العمل بنجاح...")

# أمر البداية /start مع أزرار القائمة الرئيسية
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('💻 لغات البرمجة')
    item2 = telebot.types.KeyboardButton('🛡️ الأمن السيبراني')
    item3 = telebot.types.KeyboardButton('🔐 الهكر الأخلاقي')
    item4 = telebot.types.KeyboardButton('📞 الأرقام المجانية')
    item5 = telebot.types.KeyboardButton('🔄 استرجاع الحسابات')
    markup.add(item1, item2, item3, item4, item5)
    
    welcome_text = f"أهلاً بك يا {message.from_user.first_name} في بوت الذكاء الاصطناعي المطور للأمن والبرمجة.\n\n💡 يمكنك استخدام الأزرار بالأسفل، أو كتابة أي سؤال يخطر في بالك مباشرة وسأقوم بالرد عليك فوراً بصفتي ذكاء اصطناعي غير مقيد!"
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# استقبال ومعالجة جميع الرسائل
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    chat_id = message.chat.id
    
    # 1. الردود الخاصة بالأزرار الثابتة
    if text == '💻 لغات البرمجة':
        bot.send_message(chat_id, "📌 **أفضل لغات البرمجة كبداية:**\n1. Python: للأتمتة، البرمجة، والأمن الرقمي.\n2. JavaScript: لتطوير المواقع وفهم ثغرات الويب.")
    elif text == '🛡️ الأمن السيبراني':
        bot.send_message(chat_id, "🛡️ **الأمن السيبراني يشمل:**\n- أمن الشبكات والأنظمة والتشفير.\n- التحقيق الجنائي الرقمي والاستجابة للثغرات الأمنية.")
    elif text == '🔐 الهكر الأخلاقي':
        bot.send_message(chat_id, "🔐 **قواعد الاختراق الأخلاقي:**\n- اختبار الأنظمة بتصريح رسمي ومسبق فقط.\n- مساعدة أصحاب المواقع في سد الثغرات دون إلحاق أي ضرر.")
    elif text == '📞 الأرقام المجانية':
        bot.send_message(chat_id, "⚠️ **تنبيه أمني بخصوص الأرقام:**\nالأرقام المجانية والوهمية المنتشرة عبر التطبيقات غير آمنة لحساباتك الأساسية، حيث يمكن أن تنتقل لملكية مستخدم آخر وتفقد حسابك.")
    elif text == '🔄 استرجاع الحسابات':
        bot.send_message(chat_id, "🔄 **طرق التأمين والاسترجاع:**\n1. تواصل دائماً وبشكل مباشر مع الدعم الرسمي للمنصة.\n2. فعّل ميزة التحقق الثنائي (2FA) فوراً على جميع حساباتك لحمايتها من الاختراق.")
    
    # 2. إذا كتب المستخدم أي شيء آخر، يتم إرساله للذكاء الاصطناعي المفتوح
    else:
        # إرسال رسالة "جاري التفكير..." للمستخدم حتى يأتي الرد
        thinking_msg = bot.send_message(chat_id, "🤔 جاري التفكير والرد من خلال الذكاء الاصطناعي...")
        
        try:
            # استخدام API خارجي مفتوح للذكاء الاصطناعي (بدون قيود مشددة)
            api_url = f"https://lolhuman.xyz{requests.utils.quote(text)}"
            response = requests.get(api_url, timeout=15)
            
            if response.status_code == 200:
                result = response.json()
                ai_response = result.get("result", "عذراً، لم أستطع معالجة الرد حالياً.")
                
                # مسح رسالة "جاري التفكير" وإرسال الإجابة الرسمية
                bot.delete_message(chat_id, thinking_msg.message_id)
                bot.send_message(chat_id, ai_response)
            else:
                bot.edit_message_text("❌ واجهت مشكلة في الاتصال بسيرفر الذكاء الاصطناعي، يرجى المحاولة مجدداً.", chat_id, thinking_msg.message_id)
                
        except Exception as e:
            bot.edit_message_text("⚠️ حدث خطأ أثناء جلب الرد، حاول مرة أخرى.", chat_id, thinking_msg.message_id)

# تشغيل البوت باستمرار
try:
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
except Exception as e:
    print(f"خطأ: {e}")
