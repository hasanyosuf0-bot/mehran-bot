import telebot
import os

# التوكن الجديد بتاعك مدمج هنا
TOKEN = '8985832742:AAFZd44EbyEUCWrhUS2OXFkrNMOJqflALwY'
bot = telebot.TeleBot(TOKEN)

print("🚀 البوت بدأ العمل بنجاح على جيت هاب...")

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
    
    welcome_text = f"أهلاً بك يا {message.from_user.first_name} في بوت التوجيه البرمجي والأمن السيبراني.\nاختر قسماً من القائمة بالأسفل للبدء:"
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# الردود على الأزرار
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    
    if text == '💻 لغات البرمجة':
        bot.send_message(message.chat.id, "📌 **أفضل لغات البرمجة كبداية:**\n1. Python: للأتمتة، البرمجة، والأمن الرقمي.\n2. JavaScript: لتطوير المواقع وفهم ثغرات الويب.")
            
    elif text == '🛡️ الأمن السيبراني':
        bot.send_message(message.chat.id, "🛡️ **الأمن السيبراني يشمل:**\n- أمن الشبكات والأنظمة والتشفير.\n- التحقيق الجنائي الرقمي والاستجابة للثغرات الأمنية.")
            
    elif text == '🔐 الهكر الأخلاقي':
        bot.send_message(message.chat.id, "🔐 **قواعد الاختراق الأخلاقي:**\n- اختبار الأنظمة بتصريح رسمي ومسبق فقط.\n- مساعدة أصحاب المواقع في سد الثغرات دون إلحاق أي ضرر.")
            
    elif text == '📞 الأرقام المجانية':
        bot.send_message(message.chat.id, "⚠️ **تنبيه أمني بخصوص الأرقام:**\nالأرقام المجانية والوهمية المنتشرة عبر التطبيقات غير آمنة لحساباتك الأساسية، حيث يمكن أن تنتقل لملكية مستخدم آخر وتفقد حسابك.")
            
    elif text == '🔄 استرجاع الحسابات':
        bot.send_message(message.chat.id, "🔄 **طرق التأمين والاسترجاع:**\n1. تواصل دائماً وبشكل مباشر مع الدعم الرسمي للمنصة.\n2. فعّل ميزة التحقق الثنائي (2FA) فوراً على جميع حساباتك لحمايتها من الاختراق.")
    else:
        bot.send_message(message.chat.id, "💡 يرجى اختيار أحد الأزرار المتاحة في القائمة أو كتابة /start")

# تشغيل البوت وتخطي أخطاء التعارض (Polling Conflict)
try:
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
except Exception as e:
    print(f"حدث خطأ في الاتصال: {e}")
