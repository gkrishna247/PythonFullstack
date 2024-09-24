#sql query to group data
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "employ"
)

mycursor = mydb.cursor()
a=input("Enter the first number: ")
b=input("Enter the second number: ")
squery="SELECT * FROM emp_per where empid>%s and empid<%s"
mycursor.execute(squery,(a,b))
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
