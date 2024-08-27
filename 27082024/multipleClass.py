class a:
    def __init__(self,y):
        self.x=y
    
    def display(self):
        print(self.x)

t=a(10)
n=t

class b:
    def access(self,m):
        m.display()

g=b()
g.access(n)