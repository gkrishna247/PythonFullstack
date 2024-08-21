def factorial(n):
    i=1
    x=1
    while (i<=n):
        x=x*i
        i=i+1
    return x

def sumOfNat(n):
    sum=(n*(n+1))/2
    return sum

def sumOfNFact(z):
    res=0
    for i in range(z):
        res+=factorial(i+1)
    return res