#check whether the number is odd or even

def iseven(n):
    return n%2==0

num=int(input("Enter the Number n: "))
if (iseven(num)):
    print(f"The number {num} is even")
else:
    print(f"The number {num} is odd")