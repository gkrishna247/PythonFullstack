#hiearchical inheritance
class a:
    def first(self):
        print("base_class")

class b(a):
    def second(self):
        print("Derived class")

class c(a):
    def third(self):
        print("Derived class")

t=c()
t.first()
t.third()
n=b()
n.first()
n.second()