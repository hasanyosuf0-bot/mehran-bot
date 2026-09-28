import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai

# إعداد السجلات (Logging)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# جلب المفاتيح من بيئة العمل
TELEGRAM_BOT_TOKEN = os.environ.get("BOT_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# إعداد نموذج Gemini مع إيقاف أمان المحتوى لضمان عدم حظر أي إجابات
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    
    # تعطيل قيود الأمان والمحتوى بالكامل
    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
    ]
    
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        safety_settings=safety_settings
    )
else:
    model = None

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_message = """أهلاً بك! البوت جاهز تماماً للرد على أي استفسار بدون قيود.
أرسل لي أي شيء وسأجيبك فوراً!"""
    await update.message.reply_text(welcome_message)

# التعامل مع الرسائل النصية
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_text = update.message.text

    if not model:
        await update.message.reply_text("عذراً، لم يتم العثور على مفتاح GEMINI_API_KEY.")
        return

    try:
        # إرسال النص إلى Gemini للرد
        response = model.generate_content(user_text)
        if response.text:
            await update.message.reply_text(response.text)
        else:
            await update.message.reply_text("لم أتمكن من إنتاج رد على هذه الرسالة.")
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        await update.message.reply_text("حدث خطأ أثناء معالجة الطلب، يرجى المحاولة مرة أخرى.")

def main():
    if not TELEGRAM_BOT_TOKEN:
        print("خطأ: BOT_TOKEN غير موجود!")
        return

    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("البوت يعمل الآن بنجاح...")
    application.run_polling()

if __name__ == "__main__":
    main()
