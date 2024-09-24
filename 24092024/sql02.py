import mysql.connector

#connecting to mysql
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "employ"
)

cursor = mydb.cursor()
id = input("Enter Empid: ")
sql = "select * from emp_per where empid = %s"
cursor.execute(sql, (id,))
result = cursor.fetchone()
for i in result:
    print(i)
