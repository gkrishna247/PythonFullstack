#write a python program to find 1!+2!+ . . . +n!
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

def sumOfFact(n):
    sum=0
    for i in range(n):
        sum+=factorial(i+1)
    return sum

n=int(input("Enter the value of n: "))
print("The sum of n factorial is ",sumOfFact(n))