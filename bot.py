import logging
import os
from google import genai
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    filters,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
  user_message = update.message.text
  logger.info(f"Received message: {user_message}")

  try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_message,
    )

    reply_text = response.text
    await update.message.reply_text(reply_text)

  except Exception as e:
    logger.error(f"Error generating content: {e}")
    await update.message.reply_text(
        "Sorry, an error occurred while processing your request."
    )


def main():
  if not TELEGRAM_TOKEN or not GEMINI_API_KEY:
    logger.error("Please set TELEGRAM_TOKEN and GEMINI_API_KEY environment variables.")
    return

  app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
  app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

  print("Bot is running...")
  app.run_polling()


if __name__ == "__main__":
  main()
