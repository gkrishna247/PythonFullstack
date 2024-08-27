#write a pyhton program to add 5 student marks for using array of objects
#from the following given field names
#roll no,name,tamil,english,maths

class Student:
    def _init_(self, adno, name, tamil, english, maths):
        self.adno = adno
        self.name = name
        self.tamil = tamil
        self.english = english
        self.maths = maths

    def total_marks(self):
        return self.tamil + self.english + self.maths

    def display(self):
        print(f"Admission Number: {self.adno}")
        print(f"Name: {self.name}")
        print(f"Tamil Marks: {self.tamil}")
        print(f"English Marks: {self.english}")
        print(f"Maths Marks: {self.maths}")
        print(f"Total Marks: {self.total_marks()}")

def student_details():
    adno = int(input("Enter Admission Number: "))
    name = input("Enter Name: ")
    tamil = int(input("Enter Tamil Marks: "))
    english = int(input("Enter English Marks: "))
    maths = int(input("Enter Maths Marks: "))
    return Student(adno, name, tamil, english, maths)

s = []

for i in range(5):
    print(f"\nEnter student details")
    student = student_details()
    s.append(student)

for student in s:
    student.display()