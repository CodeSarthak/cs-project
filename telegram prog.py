import time
import telebot


TOKEN = "1392448049:AAHedLc3i0cqF61kubWlOiloawlt4JHY80s"
bot = telebot.TeleBot(token=TOKEN)



@bot.message_handler(commands=['start']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, 'Hey, there! Type "/help" to get help on how to get started! ')

@bot.message_handler(commands=['help']) # help message handler
def send_welcome(message):
    bot.reply_to(message, 'Type in your admission number and password in this format to get your homework : [admission number] [password]. For example, 1234 password')
def extract_msg(message):
   msg.append(message.text)
   print(msg)
while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        time.sleep(5)









