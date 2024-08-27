class maths:
    def add(self):
        self.x=int(input("Enter value of x: "))
        self.y=int(input("Enter value of y: "))
        self.z=self.x+self.y

    def __init__(self):
        self.x=int(input("Enter value of x: "))
        self.y=int(input("Enter value of y: "))
        self.z=self.x+self.y

    def addrt(self):
        self.x=int(input("Enter value of x: "))
        self.y=int(input("Enter value of y: "))
        return self.x+self.y
    
    def addArgRt(self,n1,n2):
        return n1+n2

t=maths()
print("Total: ",t.z)
t.add()
print("Total: ",t.z)
print("Total: ",t.addrt())
num1=int(input("Enter first value: "))
num2=int(input("Enter second value: "))
print("Total: ",t.addArgRt(num1,num2))