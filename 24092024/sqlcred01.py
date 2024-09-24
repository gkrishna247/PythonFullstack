# program for perform cred operation on mysql
import mysql.connector

#connecting to mysql
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "employ"
)

#function to add data to table
def add_data():
    mycursor = mydb.cursor()
    sql = "insert into emp_per (empid, name, pos, dept) values (%s, %s, %s, %s)"
    empid = input("Enter Empid: ")
    name = input("Enter Name: ")
    pos = input("Enter Position: ")
    dept = input("Enter Department: ")
    mycursor.execute(sql, (empid, name, pos, dept))
    mydb.commit()
    print("Data inserted successfully")

#function to read data from table for particular empid
def read_data():
    mycursor = mydb.cursor()
    sql = "select * from emp_per where empid = %s"
    empid = input("Enter Empid: ")
    mycursor.execute(sql, (empid,))
    data = mycursor.fetchone()
    print(f"Empid: {data[0]}")
    print(f"Name: {data[1]}")
    print(f"Position: {data[2]}")
    print(f"Department: {data[3]}")
    

#function to update data in table 
def update_data():
    mycursor = mydb.cursor()
    sql = "update emp_per set pos = %s where empid = %s"
    empid = input("Enter Empid: ")
    pos = input("Enter Position: ")
    mycursor.execute(sql, (pos, empid))
    mydb.commit()
    print("Data updated successfully")

#function to delete data from table
def delete_data():
    mycursor = mydb.cursor()
    sql = "delete from emp_per where empid = %s"
    empid = input("Enter Empid: ")
    mycursor.execute(sql, (empid,))
    mydb.commit()
    print("Data deleted successfully")

#menu driven program
while True:
    print("1. Add Data")
    print("2. Read Data")
    print("3. Update Emp Position")
    print("4. Delete Data")
    print("5. Exit")
    ch = input("Enter your choice: ")
    if ch == "1":
        add_data()
    elif ch == "2":
        read_data()
    elif ch == "3":
        update_data()
    elif ch == "4":
        delete_data()
    elif ch == "5":
        break
    else:
        print("Invalid Choice")

#closing the connection
mydb.close()

