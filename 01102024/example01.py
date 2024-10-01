class database:
    def add_record(self,empno,name):
        self.empno=empno
        self.name=name

    def find_record(self, empno):
        # Add logic to find the record
        pass

    def update_record(self, empno, address, city, pincode):
        self.empno = empno
        self.address = address
        self.city = city
        self.pincode = pincode

    k = int(input("Enter your choice"))
    if k == 1:
        print("Add Record")
        empno = input("Empno ")
        name = input("Name ")
        data.add_record(empno, name)
    elif k == 2:
        print("Update Record")
        empno = input("Empno ")
        address = input("Address ")
        city = input("City ")
        pincode = input("Pincode ")
        data.update_record(empno, address, city, pincode)
        name=input("Name ")
        data.add_record(empno,name)
    if(k==2):
        print("Update Record")
        empno=input("Empno")
        address=input("Address")
        data.update_record(empno,address)