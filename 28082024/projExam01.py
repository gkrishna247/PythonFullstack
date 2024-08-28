class records:
    def add(self):
        print("Add")
    def delete(self):
        print("Delete")
    def update(self):
        print("Update")
    def list(self):
        print("List")
print("1.Add")
print("2.Delete")
print("3.Update")
print("4.List")
print("5.Exit")
i=1
while(i<=1):
    status=int(input("Press 5 to  exit! \n"))
    if(status==5):
        break
    else:
        m=records()
        choice=int(input("Enter Choice:"))
        if(choice==1):
            m.add()
        if(choice==2):
            m.delete()
        if(choice==3):
            m.update()
        if(choice==4):
            m.list()