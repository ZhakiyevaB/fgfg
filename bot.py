import telebot

bot = telebot.TeleBot(BOT_Token)

@bot.message_handler(commands=['start', 'help'])
def start_and_help(message):
    bot.send_message(message.chat.id, messages.START)
   
bot.polling() 

