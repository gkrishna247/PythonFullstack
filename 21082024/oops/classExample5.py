class maths:
    def add(self):
        self.a=int(input("Valur of a: "))
        self.b=int(input("Value of b: "))
        self.c=self.a+self.b
        return self.c
    
    def result(self):
        print("Result: ",self.c)


m=maths()
m.add()
m.result()