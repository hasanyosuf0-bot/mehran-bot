import os
import telebot
from telebot import types

# التوكن الجديد الخاص ببوتك @mehran_coding_bot
# ملاحظة أمنية: إذا كنت ترفع الكود على جيت هاب عام، يفضل مستقبلاً استخدام os.environ لجلب التوكن
TOKEN = '8708625165:AAFVHmdMdZe6Tyv8a_cImbsqCkN3VkidkDM'
bot = telebot.TeleBot(TOKEN)

# رسالة البداية /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('💻 لغات البرمجة')
    item2 = types.KeyboardButton('🛡️ الأمن السيبراني')
    item3 = types.KeyboardButton('🔐 الهكر الأخلاقي')
    item4 = types.KeyboardButton('📞 الأرقام الوهمية )')
    item5 = types.KeyboardButton('🔄 استرجاع الحسابات)')
    
    markup.add(item1, item2, item3, item4, item5)
    
    welcome_text = (
        f"أهلاً بك يا {message.from_user.first_name} في بوت الخدمات التعليمية والأمنية الخاص بـ @mehran_coding_bot.\n"
        "اختر أحد الأقسام من القائمة أدناه للبدء:"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# التعامل مع الأزرار والرسائل النصية
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    
    if text == '💻 لغات البرمجة':
        bot.send_message(message.chat.id, 
            "أفضل لغات البدء في البرمجة والأمن السيبراني:\n"
            "1. Python: ممتازة للاختراق والأتمتة.\n"
            "2. Bash/Shell: للتحكم بنظام لينكس.\n"
            "3. JavaScript & HTML: لتطوير الويب وفهم الثغرات (XSS).")
            
    elif text == '🛡️ الأمن السيبراني':
        bot.send_message(message.chat.id, 
            "ألأمن السيبراني ة:\n"
            "- أمن الشبكات (Network Security)\n"
            "- اختبار الفحص والتقييم (Penetration Testing)\n"
            "- التشفير وتحليل البيانات\n"
            "- الاستجابة للحوادث الرقمية.")
            
    elif text == '🔐 الهكر الأخلاقي':
        bot.send_message(message.chat.id, 
            "الهكر الأخلاقي:\n"
            "- الحصول دائماً على إذن مسبق قبل اختبار أي نظام.\n"
            "-الإبلاغ عن الثغرات ة (Responsible Disclosure).\n
            
    elif text == '📞 الأرقام الوهمية (إرشادات)':
        bot.send_message(message.chat.id, 
            "بخصوص الأرقام المجانية أو الوهمية:\n"
            "الكثير من التطبيقات المجانية توفر أرقاماً، لكنها غالباً غير آمنة وقد تُسحب وتُمنح لشخص آخر.\n"
            "يُفضل استخدام أرقام حقيقية خاصة لتأمين حساباتك الشخصية وعدم استخدام خدمات مجهولة.")
            
    elif text == '🔄 استرجاع الحسابات (نصائح)':
        bot.send_message(message.chat.id, 
            "نصائح لاسترجاع وتأمين الحسابات:\n"
            "1 
            "2. تفعيل المصادقة الثنائية (2FA) فوراً.\n"
            "3. استرجاع الحسابات وسرقتها.")
    else:
        bot.send_message(message.chat.id, "عذراً، لم أفهم الأمر. استخدم القائمة أو اضغط /start")

# تشغيل البوت باستمرار
print("Bot @mehran_coding_bot is starting...")
bot.infinity_polling()
