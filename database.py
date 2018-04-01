import sqlite3
import random


def getJoke():
    conn = sqlite3.connect('db/maindb.db')
    c = conn.cursor()
    c.execute('SELECT * FROM joke WHERE id')
    row = c.fetchall()
    row = row[random.randrange(0,len(row))]
    return row[1]
    c.close()