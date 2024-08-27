
ispalindrome = lambda s: s==s[::-1]
a=input("Enter the string to check it is palindrome: ")
if (ispalindrome(a)):
    print(f"{a} is palindrome")
else:
    print(f"{a} is not a palindrome")