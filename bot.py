import os
import telebot
from telebot import types

TOKEN = os.getenv('TOKEN', '8708625165:AAF63kNHGMeqNhdByOqEMGCwTA1q941_tAk')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Programming Services')
    btn2 = types.KeyboardButton('Cyber Security')
    btn3 = types.KeyboardButton('Account Recovery')
    btn4 = types.KeyboardButton('Social Media Ads')
    btn5 = types.KeyboardButton('Technical Support')
    
    markup.add(btn1, btn2, btn3, btn4, btn5)
    
    welcome_message = (
        f"Welcome {message.from_user.first_name} to Mehran Coding Bot (@mehran_coding_bot).\n\n"
        "Your automated assistant for programming, security, and digital services.\n"
        "Please choose a section from the menu below:"
    )
    bot.send_message(message.chat.id, welcome_message, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    txt = message.text
    
    if txt == 'Programming Services':
        res = (
            "Programming & Development Services:\n\n"
            "1. Web Development (Frontend & Backend).\n"
            "2. Advanced Telegram Bots.\n"
            "3. Mobile App Solutions.\n"
            "4. Custom Python & JavaScript Scripts."
        )
        bot.send_message(message.chat.id, res)
        
    elif txt == 'Cyber Security':
        res = (
            "Cyber Security & Ethical Hacking:\n\n"
            "1. Penetration Testing & Vulnerability Assessment.\n"
            "2. Server & Database Hardening.\n"
            "3. Information Security Consultations.\n\n"
            "Note: All services comply with ethical hacking standards."
        )
        bot.send_message(message.chat.id, res)
        
    elif txt == 'Account Recovery':
        res = (
            "Account Recovery Services:\n\n"
            "1. Recover hacked or lost social media accounts.\n"
            "2. Apply advanced security layers.\n"
            "3. Restore banned or stolen channels."
        )
        bot.send_message(message.chat.id, res)
        
    elif txt == 'Social Media Ads':
        res = (
            "Social Media & Advertising:\n\n"
            "1. Paid ad campaigns management.\n"
            "2. Growth strategies and engagement.\n"
            "3. Digital marketing consultation."
        )
        bot.send_message(message.chat.id, res)
        
    elif txt == 'Technical Support':
        res = (
            "Technical Support:\n\n"
            "For direct contact and custom requests:\n"
            "Developer: @hasanyosuf0-bot"
        )
        bot.send_message(message.chat.id, res)
        
    else:
        bot.send_message(message.chat.id, "Invalid option. Please use the menu or type /start.")

if __name__ == '__main__':
    print("Bot is running successfully...")
    bot.infinity_polling()
