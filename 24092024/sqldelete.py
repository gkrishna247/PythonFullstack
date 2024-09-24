#program to perform sql delete
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "employ"
)

cursor = mydb.cursor()
id = input("Enter Empid: ")
sql = "delete from emp_per where empid = %s"
cursor.execute(sql, (id,))
mydb.commit()
print("Data deleted successfully")

