class cs:
    def input_record(self):
        self.adno=input("Adno: ")
        self.name=input("Name: ")
        self.python=input("Python: ")
        self.java=input("Java: ")
    def output_record(self):
        print(self.adno)
        print(self.name)
        print(self.python)
        print(self.java)
class ec:
    def input_record(self):
        self.adno=input("Adno: ")
        self.name=input("Name: ")
        self.digital=input("Digital: ")
        self.network=input("Network: ")
    def output_record(self):
        print(self.adno)
        print(self.name)
        print(self.digital)
        print(self.network)
class mech:
    def input_record(self):
        self.adno=input("Adno: ")
        self.name=input("Name: ")
        self.mech1=input("Mech1: ")
        self.mech2=input("Mech2: ")
    def output_record(self):
        print(self.adno)
        print(self.name)
        print(self.mech1)
        print(self.mech2)

a=cs()
a.input_record()
a.output_record()
b=ec()
b.input_record()
b.output_record()
c=mech()
c.input_record()
c.output_record()