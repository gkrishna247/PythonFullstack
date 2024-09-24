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
    sql = "insert into emp_per (empid, name, pos, dept, salid) values (%s, %s, %s, %s, %s)"
    empid = input("Enter Empid: ")
    name = input("Enter Name: ")
    pos = input("Enter Position: ")
    dept = input("Enter Department: ")
    salid = input("Enter Salary ID: ")
    mycursor.execute(sql, (empid, name, pos, dept, salid))
    mydb.commit()
    print("Data inserted successfully")

#function to read data from table
def read_data():
    mycursor = mydb.cursor()
    sql = "select * from emp_per"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for row in result:
        print(row)

#function to update data in table
def update_data():
    mycursor = mydb.cursor()
    sql = "update emp_per set name = %s where empid = %s"
    name = input("Enter Name: ")
    empid = input("Enter Empid: ")
    mycursor.execute(sql, (name, empid))
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
    print("3. Update Data")
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


"""
empid	int(11)	NO	PRI	NULL		
name	varchar(50)	NO		NULL		
pos	varchar(50)	NO		NULL		
dept	varchar(50)	NO		NULL		
salid	int(11)	YES	MUL	NULL

empid	int(11)	YES	MUL	NULL		
salid	int(11)	NO	PRI	NULL		
salary	int(11)	YES		NULL		
joindate	date	YES		NULL		"""
