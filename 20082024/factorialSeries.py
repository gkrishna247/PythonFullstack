def fact(n):
    g=1
    i=1
    while (i<=n):
        g=g*i
        i=i+1
    return g

x=int(input("Value of x: "))
j=1
sum=0
while(j<=x):
    sum=sum+fact(j)
    j=j+1

print("Result: ",sum)