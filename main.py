import telebot
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Men haqimda")
    btn2 = types.KeyboardButton("Loyihalarim")
    btn3 = types.KeyboardButton("Kontakt")
    btn4 = types.KeyboardButton("Bilimlarim")
    keyboard.add(btn1, btn2)
    keyboard.add(btn3, btn4)
    text = "Assalom alaykum, men Farrux Xudarganov. \nBu mening portfolio botim. \nQuyidagi bo'limlardan birini tanlang"

    bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.message_handler(func=lambda m: m.text == "Men haqimda")
def aboutme_handler(message):
    text = "Men Farrux frontend engineermen. React.js & Next.js specialistman"
    
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda m: m.text == "Loyihalarim")
def projects_handler(message):
    text = """## Loyihalarim

* **Streamline Landing Sahifasi**
  * **Veb-sayt:** [Streamline Landing Page](https://streamline-xi.vercel.app/)

* **Matnni Lotindan Kirillga yoki Kirilldan Lotinga o'tkazuvchi bot**
  * **Telegram bot:** [@krilllatin_cnv_bot](https://t.me/@krilllatin_cnv_bot)"""
    
    
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

@bot.message_handler(func=lambda m: m.text == "Kontakt")
def contact_handler(message):
    text = "Aloqa qismi tez orada qoshiladi"
    
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Telegram", url="https://t.me/xudarganov_f")
    btn2 = types.InlineKeyboardButton("GitHub", url="https://github.com/farruxxudarganov")
    keyboard.add(btn1, btn2)
    
    bot.send_message(message.chat.id, text, reply_markup=keyboard)
@bot.message_handler(func=lambda m: m.text == "BIlimlarim")
def skills_handler(massage):
    text = "Men HTML, CSS Python texnalogiyalarini bilaman"
    bot.send_message(massage.chat.id, text)
bot.infinity_polling()
