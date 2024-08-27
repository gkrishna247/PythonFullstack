#write a python program to find a n!

def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

n=int(input("Enter the value of n: "))
print("Factorial: ",factorial(n))