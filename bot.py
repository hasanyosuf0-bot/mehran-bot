import os
import telebot
import google.generativeai as genai
from google.generativeai import types

# جلب توكن البوت ومفتاح جيميناي من متغيرات البيئة
BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# التحقق من وجود المفاتيح
if not BOT_TOKEN:
    raise ValueError("الرجاء تعيين متغير البيئة BOT_TOKEN")

if not GEMINI_API_KEY:
    raise ValueError("الرجاء تعيين متغير البيئة GEMINI_API_KEY")

# إعداد جيميناي
genai.configure(api_key=GEMINI_API_KEY)

# إعدادات السلامة
safety_settings = [
    {
        "category": types.HarmCategory.HARM_CATEGORY_HARASSMENT,
        "threshold": types.HarmBlockThreshold.BLOCK_NONE,
    },
    {
        "category": types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        "threshold": types.HarmBlockThreshold.BLOCK_NONE,
    },
    {
        "category": types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        "threshold": types.HarmBlockThreshold.BLOCK_NONE,
    },
    {
        "category": types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        "threshold": types.HarmBlockThreshold.BLOCK_NONE,
    },
]

generation_config = {
    "temperature": 0.7,
}

# تحسين صياغة تعليمات النظام باللغة العربية لتكون واضحة للنموذج
system_instruction = (
    "أنت مساعد ذكاء اصطناعي شخصي ومبدع محتوى. "
    "أجب على أسئلة المستخدمين بشكل مباشر، واضح، ودقيق، "
    "وقدم المعلومات المطلوبة بكل احترافية وموضوعية."
)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    safety_settings=safety_settings,
    system_instruction=system_instruction
)

# بدء تشغيل بوت تيليجرام
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! أنا بوت الذكاء الاصطناعي، كيف يمكنني مساعدتك اليوم؟")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # إرسال رسالة انتظار للمستخدم
        waiting_msg = bot.reply_to(message, "جاري التفكير...")
        
        # توليد الرد من نموذج جيميناي
        response = model.generate_content(message.text)
        
        # التأكد من أن الرد يحتوي على نص
        if response.text:
            bot.edit_message_text(response.text, chat_id=message.chat.id, message_id=waiting_msg.message_id)
        else:
            bot.edit_message_text("عذراً، لم أتمكن من توليد رد مناسب.", chat_id=message.chat.id, message_id=waiting_msg.message_id)
            
    except Exception as e:
        # في حال حدث خطأ، قم بتحديث رسالة الانتظار أو إرسال رسالة جديدة
        try:
            bot.edit_message_text(f"حدث خطأ أثناء معالجة طلبك: {str(e)}", chat_id=message.chat.id, message_id=waiting_msg.message_id)
        except:
            bot.reply_to(message, f"حدث خطأ أثناء معالجة طلبك: {str(e)}")

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
