def list_all(a,b):
    inn=a
    while (inn<=b):
        print("RollNo: ",inn)
        inn=inn+1

i=int(input("Enter intial Rollno: "))
f=int(input("Enter final Roll no: "))
list_all(i,f)
