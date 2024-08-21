class maths:
    def add(self):
        self.a=int(input("Valur of a: "))
        self.b=int(input("Value of b: "))
        c=self.a+self.b
        return c
    
m=maths()
print(m.add())