#program to perform sql bulk insert
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "employ"
)

cursor = mydb.cursor()
insert_bulk = "insert into emp_per (empid, name, pos, dept) values (%s, %s, %s, %s)"
values = (2, "Rahul", "Manager", "HR"), (3, "Rohit", "Developer", "IT"), (4, "Raj", "Tester", "QA")
cursor.executemany(insert_bulk, values)
mydb.commit()
print("Data inserted successfully")



