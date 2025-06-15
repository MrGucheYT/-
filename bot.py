import telebot
from config import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я Telegram бот. Я научу тебя заботиться об окружающей среде!")

@bot.message_handler(commands=['sortirovka'])
def send_sortirovka(message):
    bot.reply_to(message, "Мусорный бак зелёного цвета - для стекла. А в красный бак нужно класть металл. В синий контейнер - бумагу, а в жёлтый - пластик")

bot.polling()