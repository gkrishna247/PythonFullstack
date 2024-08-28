#multilevel inheritance
class a:
    def first(self):
        print("base_class")

class b(a):
    def second(self):
        print("derived class")

class c(b):
    def third(self):
        print("Derived class")

t=c()
t.first()
t.second()
t.third()