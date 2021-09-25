import telebot
import time 
from telebot import types
from datetime import datetime


current_datetime = datetime.now()


current_date = datetime.now().date()


bot=telebot.TeleBot("2037859631:AAF3y3F-oev6JLOZQ5QNrOwewzxy4QB1TFE")

@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.reply_to(message, "Salom men siz bilan suhbatlashaman men bilan aslo zerikmaysiz  HURMATLI   "+ str(message.from_user.first_name))
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Salom':
         bot.send_message(message.chat.id, 'Salom. Qalesiz  '+ str(message.from_user.first_name))
    elif message.text == 'Hayr':
         bot.send_message(message.chat.id, "Hayr ko'rishguncha " + str(message.from_user.first_name))
    elif message.text == "Bo'pti":
         bot.send_message(message.chat.id, "Bo'pti ko'rishguncha  " + str(message.from_user.first_name))
    elif message.text == "Qalesan":
         bot.send_message(message.chat.id, "Zo'r, o'zizchi?")
    elif message.text == "Zo'r":
        bot.send_message(message.chat.id, "Ok. Har doim zo'r bo'lib yuring")
    elif message.text == "Zor":
        bot.send_message(message.chat.id, "Ok. Har doim zo'r bo'lib yuring")
    elif message.text == "Nima gap":
        bot.send_message(message.chat.id, "Zo'r")
    elif message.text == "Isming nima":
        bot.send_message(message.chat.id, "Bot")
    elif message.text == "Nma gap":
        bot.send_message(message.chat.id, "Zo'r")
    elif message.text == "Nega":
        bot.send_message(message.chat.id, "Ozi!!!!")
    elif message.text == "Lalala":
        bot.send_message(message.chat.id, "Tinchlimi" + str(message.from_user.first_name))
    elif message.text == "/soat":
        bot.send_message(message.chat.id, current_datetime)
    elif message.text == "/sana":
        bot.send_message(message.chat.id, current_date)
    elif message.text == "Admin":
        bot.send_message(message.chat.id, "@Abdulloh_ahmadjonov")
    elif message.text == "Qandaysiz":
        bot.send_message(message.chat.id, "Zo'r")
    elif message.text == "Zor":
        bot.send_message(message.chat.id, "Unda Yahshi  😊 ")
    elif message.text == "Yil":
        bot.send_message(message.chat.id, time.localtime()[:3])
    elif message.text == "Nimaga":
        bot.send_message(message.chat.id, "Shunchaki")
    elif message.text == "Hmm":
        bot.send_message(mage.chat.id, "Hmm")
    elif message.text == "Ok":
        bot.send_message(message.chat.id, "👌")
    elif message.text == "":
        bot.send_message(message.chat.id, "")
    elif message.text == "":
        bot.send_message(message.chat.id, "")
    elif message.text == "/data":
        bot.send_message(message.chat.id, current_datetime)
    elif message.text == "Sana":
        bot.send_message(message.chat.id, current_date)




bot.send_message(message.chat.id,"Bunday shahar topilmadi!")


bot.polling(none_stop= True)
bot.polling()
