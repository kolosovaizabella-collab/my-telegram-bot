import telebot
import os

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет 👋 Я твой личный бот, работаю 24/7!")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "Доступные команды:\n/start — запустить\n/help — помощь")

@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    bot.reply_to(message, "Я получил твое сообщение!  Скоро отвечу:)")

print("Бот запущен...")
bot.infinity_polling()
