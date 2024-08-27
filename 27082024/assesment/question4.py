#sum of squares of n odd number

def sumOddSquare(n):
    sum=0
    for i in range(1,2*n,2):
        sum+=i**2
    return sum

n=int(input("Enter the value of n: "))
print("THe sum of square oF n odd numbers is ",sumOddSquare(n))