# coding: utf-8
import datetime

date = str(datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S"))


def log(message, ANSWER):
	user = message.from_user.first_name+" "+message.from_user.last_name
	nameFile = "logs/log-" + str(datetime.date.today())+" "+user+ ".txt"
	logText = "Сообщение от {0} {1}. (id = {2}) \n Текст = {3}".format(message.from_user.first_name, message.from_user.last_name,str(message.from_user.id), message.text)
	
	
	#Вывод в консоль
	print("\n ------\n")
	print(date+"\n")
	print(logText+"\n")
	print("Ответ: "+ANSWER+"\n")
	
	
	
	#Вывод в файл
	logFille = open(nameFile, "a", encoding='utf-8')
	logFille.write("\n ------------------------------------------------------\n")
	logFille.write(date+"\n")
	logFille.write(logText+"\n")
	logFille.write("Ответ: "+ANSWER+"\n")
	logFille.close()