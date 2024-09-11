import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="", database="dummy")

mycursor = mydb.cursor()

sql1="select * from ksr"
mycursor.execute(sql1)
data = mycursor.fetchall()

for row in data:
    print(row)

print("Data Fetched Successfully")

#insert

sql = "insert into ksr (rollno, name, address, city ) values (%s, %s, %s, %s)"

rollno = input("Enter Roll No: ")
name = input("Enter Name: ")
address = input("Enter Address: ")
city = input("Enter City: ")

mycursor.execute(sql, (rollno, name, address, city))

mydb.commit()

print("Data Inserted Successfully")
