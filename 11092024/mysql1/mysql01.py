import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="", database="dummy")

mycursor = mydb.cursor()
sql="insert into ksr values(1,'raj','chennai','tamilnadu')"
mycursor.execute(sql)
mydb.commit()