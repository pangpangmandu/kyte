import sqlite3
import random
import string
import time


conn = sqlite3.connect('../db.sqlite3')
cur = conn.cursor()

while True :
    cur.execute("SELECT * FROM match_profile WHERE running = 1")
    quelist = cur.fetchall()
    print("the number of user" + str(len(quelist)))
    if len(quelist) > 3 :
        tmp = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        for i in range(0,2):
            cur.execute("UPDATE match_profile SET running = 0 WHERE id = "+str(quelist[i][0]))
            cur.execute("INSERT INTO match_matcheduser (chatroom, user_id) VALUES ('"+tmp+"', '"+str(quelist[i][0])+"')")
        conn.commit()
    time.sleep(1)


