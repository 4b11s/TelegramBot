import sqlite3
import random

#def register(id_tg,id_vk):
#    try:
#        if  id_vk == 0:
#            conn = sqlite3.connect('db/maindb.db')
#            c = conn.cursor()
#            c.execute("INSERT INTO users (id_tg) VALUES ('{0}')".format(id_tg))
#            conn.commit()
#            c.close()
#    except:
#        print("Ошибка №2")
#        main.bot.send_message(id_tg, "Неизвестная ошибка, возможно вы уже зарегестрированы,\n"
#                                     "эсли это так, не переживайте")
#
#        conn = sqlite3.connect('db/maindb.db')
#        c = conn.cursor()
#        c.execute("INSERT INTO users (id_vk) VALUES ('{0}')".format(id_tg))
#        conn.commit()
#        c.close()


def getJoke():
    conn = sqlite3.connect('db/maindb.db')
    c = conn.cursor()
    c.execute('SELECT * FROM joke WHERE id')
    row = c.fetchall()
    row = row[random.randrange(0,len(row))]
    return row[1]
    c.close()