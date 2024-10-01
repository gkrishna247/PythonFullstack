from mysql.connector import Error

import mysql.connector

try:
    # Connect to MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student_db"
    )

    if mydb.is_connected():
        print("Connected to MySQL database")

    # Create a cursor object to interact with the database
    cursor = mydb.cursor()

    # Create the student_master table
    create_student_master = """
    CREATE TABLE IF NOT EXISTS student_master (
        adno INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        address VARCHAR(255),
        city VARCHAR(100),
        pincode VARCHAR(10)
    );
    """
    cursor.execute(create_student_master)
    print("student_master table created successfully.")

    # Create the student_mark table
    create_student_mark = """
    CREATE TABLE IF NOT EXISTS student_mark (
        mark_id INT AUTO_INCREMENT PRIMARY KEY,
        adno INT,
        term VARCHAR(20),
        tamil INT,
        english INT,
        maths INT,
        total INT,
        FOREIGN KEY (adno) REFERENCES student_master(adno)
    ) AUTO_INCREMENT = 1001;
    """
    cursor.execute(create_student_mark)
    print("student_mark table created successfully.")

    # Insert a record into student_master
    insert_student_master = """
    INSERT INTO student_master (name, address, city, pincode)
    VALUES (%s, %s, %s, %s);
    """
    student_data = ("John Doe", "123 Main St", "Chennai", "600001")
    cursor.execute(insert_student_master, student_data)
    mydb.commit()
    print("Record inserted into student_master.")

    # Get the last inserted adno
    adno = cursor.lastrowid

    # Insert a record into student_mark
    insert_student_mark = """
    INSERT INTO student_mark (adno, term, tamil, english, maths, total)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    mark_data = (adno, "Term 1", 85, 90, 80, 255)
    cursor.execute(insert_student_mark, mark_data)
    mydb.commit()
    print("Record inserted into student_mark.")

    # Update address, city, pincode in student_master
    update_student_master = """
    UPDATE student_master
    SET address = %s, city = %s, pincode = %s
    WHERE adno = %s;
    """
    update_data = ("456 New St", "Coimbatore", "641001", adno)
    cursor.execute(update_student_master, update_data)
    mydb.commit()
    print("Record updated in student_master.")

    # Update total marks in student_mark for all students
    update_total_marks = """
    UPDATE student_mark
    SET total = tamil + english + maths;
    """
    cursor.execute(update_total_marks)
    mydb.commit()
    print("Total marks updated for all students in student_mark.")

    # Delete a record from student_master
    delete_student_master = """
    DELETE FROM student_master WHERE adno = %s;
    """
    delete_data = (adno,)
    cursor.execute(delete_student_master, delete_data)
    mydb.commit()
    print("Record deleted from student_master.")

    # Delete a record from student_mark
    delete_student_mark = """
    DELETE FROM student_mark WHERE mark_id = %s;
    """
    delete_data = (1001,)
    cursor.execute(delete_student_mark, delete_data)
    mydb.commit()
    print("Record deleted from student_mark.")

except Error as e:
    print(f"Error: {e}")
finally:
    if mydb.is_connected():
        cursor.close()
        mydb.close()
        print("Database connection closed.")