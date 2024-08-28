class addition:
    def input(self):
        self.a=int(input("Enter first Number: "))
        self.b=int(input("Enter Second Number: "))

class two(addition):
    def total(self):
        t=self.a+self.b
        print("Result: ",t)

t=two()
t.input()
t.total()