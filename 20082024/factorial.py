
def factorial(n):
    i=1
    x=1
    while (i<=n):
        x=x*i
        i=i+1
    return x

def myFun(n1,n2):
    return factorial(n1)/factorial(n2)

print(myFun(3,2))