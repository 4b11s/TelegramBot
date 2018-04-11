import sqlite3
import random
randomStr = 1
def getJoke():
	global randomStr
	conn = sqlite3.connect('db/maindb.db')
	c = conn.cursor()
	c.execute('SELECT COUNT(*) FROM joke')
	countBd = c.fetchall()
	countBd = str(countBd[0])
	countBd = countBd.replace('(','')
	countBd = countBd.replace(')','')
	countBd = countBd.replace(',','')
	randomStr = random.randrange(0,int(countBd))
	c.execute('SELECT jokeText FROM joke WHERE id = {}'.format(randomStr))
	row = c.fetchall()
	c.close
	return row[0]

def like():
	global randomStr
	conn = sqlite3.connect('db/maindb.db')
	c = conn.cursor()
	c.execute('UPDATE joke SET quaLike = quaLike+1 WHERE id = {}'.format(randomStr))
	conn.commit()
	c.close
	