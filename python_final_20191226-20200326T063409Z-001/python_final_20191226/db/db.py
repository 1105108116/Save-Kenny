# db.py
import mysql.connector

con = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="game"
)

cursor = con.cursor()

#make a function to access the db
def user_login(tup):
    try:
        cursor.execute("SELECT * FROM player WHERE user_id=%s AND password=%s",tup)
        return (cursor.fetchone())
    except:
        return False

def user_record(tup):
    try:
        cursor.execute("INSERT INTO record(user_id,datetime,score,level) VALUES(%s,%s,%s,%s)",tup)
        con.commit()
        return (cursor.fetchone())
    except:
        return False