class maths:
    def add(self):
        self.x=int(input("Enter value of x: "))
        self.y=int(input("Enter value of y: "))
        self.z=self.x+self.y

t=maths()
t.add()
print("Total: ",t.z)
        