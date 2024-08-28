class student:
    def __init__(self):
        self.adno=input("Adno: ")
        self.name=input("Name: ")

listt=[]
listt.append(student())
listt.append(student())
listt.append(student())
for i in listt:
    print("Ad.No: ",i.adno)
    print("Name: ",i.name)