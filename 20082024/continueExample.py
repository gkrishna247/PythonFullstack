def list_all(a,b):
    inn=a
    while (inn<=b):
        if (inn==8):
            inn=inn+1
            continue
        print("RollNo: ",inn)
        inn=inn+1

i=int(input("Enter intial Rollno: "))
f=int(input("Enter final Roll no: "))
list_all(i,f)
