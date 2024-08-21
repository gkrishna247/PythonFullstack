
i=1
f=open("21082024/empData2.xls",'a')

while (i==2):

    empno=input("EmpNo: ")
    empname=input("EmpName: ")
    address=input("Address: ")
    city=input("City: ")
    phone_no=input("PhoneNo: ")



    f.write("\nEmpNo: \t"+empno)
    f.write("\nEmpName: \t"+empname)
    f.write("\nAddress: \t"+address)
    f.write("\nCity: \t"+city)
    f.write("a\nPhoneNo: \t"+phone_no)
  
    print("Enter 1 to add another\nEnter 2 to Exit")
    i=int(input("Enter 1 to add another"))
                
f.close()