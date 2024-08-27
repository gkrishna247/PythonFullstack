class employee:
    def __init__(self,x):
        self.x=10   #parameter constructor
        self.y=20   #Default Constructor
    
    def access(self):
        self.z=30

n=employee(10)
n.access()
print(n.x)
print(n.y)
print(n.z)