import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="", database="dummy")

mycursor = mydb.cursor()\

sql1="select * from ksr"
mycursor.execute(sql1)

# Fetch the result of the query
result = mycursor.fetchall()

# Print the fetched results
for row in result:
    print(row)

print("Data Fetched Successfully")