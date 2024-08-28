class one:
    def first(self):
        print("First Number")

class two(one):     #Single inheritancee
        def second(self):
            print("Second Number")

t=two()
t.second()
t.first()
