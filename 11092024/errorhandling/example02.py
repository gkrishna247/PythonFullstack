# program to demonstrate exception handling
try:
    a=1
    b=0
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Division by zero is not allowed")
print("bye")