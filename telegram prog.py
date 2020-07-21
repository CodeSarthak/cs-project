import telebot
import time
bot_token='1392448049:AAHTH2h74FL8xrVsOPmwoVduifTiRGBylMo'
bot = telebot.TeleBot(token=bot_token)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'Welcome , enter your admission no. and passwd')
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message,'To start your bot enter your admission no. and passwd')
    


