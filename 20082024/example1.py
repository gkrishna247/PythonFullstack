def add(a,b):
    c=a+b
    return c

def square(k):
    t=k*k
    return t

x=int(input("Enter x value: "))
y=int(input("Enter y value: "))
z= add(x,y)
result=square(z)
print("Result:",result)