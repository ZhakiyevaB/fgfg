import telebot
import os
from env import BOT_Token
bot = telebot.TeleBot(BOT_Token)
Token = os.getenv('BOT_Token')
@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, 'Я бот для игр, выберите ниже игру:')
   
bot.polling() 