class student:
    clg="ksr college fo technology"
    dt="nammakkal"
    pincode="637215"
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
    print("CollegeName: ",i.clg)
    print("District: ",i.dt)
    print("PinCode: ",i.pincode)
