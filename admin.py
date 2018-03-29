import log


def checkPermishen(id):
	adminId = 431839224
	if int(id) == adminId:
		return 1;
	else:
		return 0;

def getLog(message):
	chek = checkPermishen(message.chat.id)
	if chek == 1:
		logFile = log.getLogFile()
		return logFile
	else:
		return "Простите, но у вас нет прав на это"