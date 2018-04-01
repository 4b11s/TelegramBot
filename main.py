import telebot
from config import *
import urllib.request as urll3
import log
import database
from parsing import getImg
import admin

gtmEnter = False

bot = telebot.TeleBot(token) #Автаризирует бота
print(bot.get_me()) #Выводит информацию о боте


def translet(name): #Замена русских букв на англ
    for key in slovar:
        name = name.replace(key, slovar[key])
    return name

	
	
@bot.message_handler(func=lambda message: gtmEnter == False, commands=['start']) #Команда начала роботы
def CommandStart(message):
    bot.send_message(message.chat.id, startText)
    log.log(message, startText)	
	
	
	
@bot.message_handler(func=lambda message: gtmEnter == False, commands=['joke']) #Команда выдающая шутки
def CommandJoke(message):
    joke = database.getJoke()
    bot.send_message(message.chat.id, joke)
    log.log(message, "/joke_@"+joke)


	
	
@bot.message_handler(func=lambda message: gtmEnter == False, commands=['help']) #Команда помощи
def CommandHelp(message):
	bot.send_message(message.chat.id, helpText)
	log.log(message, helpText)



@bot.message_handler(func=lambda message: gtmEnter == False, commands=['gtIm'])#Команда поиска картинки
def CommandGtIm(message):
		bot.send_message(message.chat.id, "Введите запрос")
		global gtmEnter
		gtmEnter = True


		
@bot.message_handler(func=lambda message: gtmEnter == True)
def sendGtmIm(message):
	try:
		global gtmEnter
		gtmEnter = False
		message_text = message.text
		img = getImg(message_text)
		log.log(message, "Картинка по запросу:"+"\n       "+img)
		imgName = "src/img/request/"+translet(message_text)+translet(" "+message.from_user.first_name)+translet(" "+message.from_user.last_name) + ".jpg"
		urll3.urlretrieve(img,imgName)
		img = open(imgName, 'rb')
		bot.send_chat_action(message.from_user.id, 'upload_photo')
		bot.send_photo(message.from_user.id,img)
		img.close()
	except:
		print("Ошибка в методе sendGtmIm")
		bot.send_message(message.chat.id, "Неизвестная ошибка, возможно вы не ввели запрос или сервер с картинками не доступен")

		
@bot.message_handler(content_types=['text']) #Реакции на текст
def textconfig(message):
	erorText = "Я не понимаю, введи /help"
	bot.send_message(message.chat.id, erorText)
	log.log(message, erorText)
	
bot.polling(none_stop=True, interval=0) #Запускает цикл програмы