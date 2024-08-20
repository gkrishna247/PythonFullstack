a=[]
n=int(input("Enter how many students: "))
i=0
while (i<n):
    name=input("name: ")
    a.append(name)
    i=i+1

print(a)

for i in a:
    print(i)