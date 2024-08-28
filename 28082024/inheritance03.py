class addition:
    def input_add(self):
        self.a=int(input("Enter first Number: "))
        self.b=int(input("Enter Second Number: "))

class subtraction:
    def input_sub(self):
        self.c=int(input("value 1: "))
        self.d=int(input("value 2: "))

class result(addition,subtraction):
    def total(self):
        t=self.a+self.b
        g=self.c-self.d
        print("Result: ",t)
        print("Result: ",g)

t=result()
t.input_add()
t.input_sub()
t.total()