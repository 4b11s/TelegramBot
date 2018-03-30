import telebot
from config import *
import urllib.request as urll3
import log
import database
from parsing import getImg
import admin


bot = telebot.TeleBot(token) #Автаризирует бота
print(bot.get_me()) #Выводит информацию о боте

def translet(name): #Замена русских букв на англ
    for key in slovar:
        name = name.replace(key, slovar[key])
    return name

	
	
@bot.message_handler(commands=['start']) #Команда начала роботы
def CommandStart(message):
    bot.send_message(message.chat.id, startText)
    log.log(message, startText)	
	
	
	
@bot.message_handler(commands=['joke']) #Команда выдающая шутки
def CommandJoke(message):
    joke = database.getJoke()
    bot.send_message(message.chat.id, joke)
    log.log(message, "/joke_@"+joke)


@bot.message_handler(commands=['help']) #Команда помощи
def CommandHelp(message):
	bot.send_message(message.chat.id, helpText)
	log.log(message, helpText)





@bot.message_handler(commands=['gtIm'])#Команда поиска картинки
def CommandGtIm(message):
    try:
        bot.send_message(message.chat.id, gtIm)
        message_text = message.text
        message_text = message_text.replace("/gtIm","")
        img = getImg(message_text)
        log.log(message, gtIm+"\n       "+img)
        imgName = "src/img/request/"+translet(message_text)+translet(" "+message.from_user.first_name)+translet(" "+message.from_user.last_name) + ".jpg"
        urll3.urlretrieve(img,imgName)
        img = open(imgName, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id,img)
        img.close()
    except:
        print("Ошибка N1\n")
        bot.send_message(message.chat.id, "Неизвестная ошибка, возможно вы не ввели запрос или сервер с картинками не доступен")

#@bot.message_handler(commands=['getlog']) #Команда получения логов
#def CommandgetLog(message):
#	otv = admin.getLog(message)
#	if type(otv) == str:
#		bot.send_message(message.chat.id, otv)
#	else:
#		bot.send_chat_action(message.from_user.id, 'upload_fille')
#		bot.send_fille(message.from_user.id,otv)
#	log.log(message, otv)	

@bot.message_handler(content_types=['text']) #Реакции на текст
def textconfig(message):
    bot.send_message(message.chat.id, erorText)
    log.log(message, erorText)
	
	
	
	
bot.polling(none_stop=True, interval=0) #Запускает цикл програмы
