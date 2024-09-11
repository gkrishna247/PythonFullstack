#example python program for sql update operation
import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user="root", password="", database="dummy")

mycursor = mydb.cursor()

sql = "update ksr set name = 'raju' where rollno = 1"

mycursor.execute(sql)

mydb.commit()
