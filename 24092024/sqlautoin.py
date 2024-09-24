#program for sql auto increment
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_db"
)
mycursor = mydb.cursor()
#insert data into table
squery = "INSERT INTO student (name,address,city) VALUES (%s,%s,%s)"
val = ("Raj","Mumbai","Mumbai")
val = ("Raja","delhi","delhi")
mycursor.execute(squery,val)
mydb.commit()
print(mycursor.rowcount,"record inserted.")
#display data
squery = "SELECT * FROM student"
mycursor.execute(squery)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

