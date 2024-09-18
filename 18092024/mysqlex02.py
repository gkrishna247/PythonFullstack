#program for performing mysql cred operations
import mysql.connector

#connecting to mysql
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "dummy"
)

#creating cursor object
mycursor = mydb.cursor()

#sql query
sql = "insert into ksr (rollno, name, address, city ) values (%s, %s, %s, %s)"

#taking input from user
rollno = input("Enter Roll No: ")
name = input("Enter Name: ")
address = input("Enter Address: ")
city = input("Enter City: ")

#executing the query
mycursor.execute(sql, (rollno, name, address, city))

#commiting the changes
mydb.commit()
print("Data inserted successfully")
#closing the connection
mydb.close()

