import fileModule
i=1
while (i==1):

    empno=input("EmpNo: ")
    empname=input("EmpName: ")
    address=input("Address: ")
    city=input("City: ")
    phone_no=input("PhoneNo: ")



    fileModule.write(empno,empname,address,city,phone_no)
  
    print("Enter 1 to add another\nEnter 2 to Exit")
    i=int(input("Enter your option: "))
