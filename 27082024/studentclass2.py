class student:
    def __init__(self):
        self.adno=int(input("Adno: "))
        self.name=input("Name: ")
        self.address=input("Address: ")

t=[]
t.append(student())
t.append(student())
t.append(student())

for r in t:
    print("Admission NO: ")
    print("Name: ")
    print("Address: ")