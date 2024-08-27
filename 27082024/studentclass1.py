class student:
    def input_master(self):
        self.adno=int(input("Adno: "))
        self.name=input("Name: ")
        self.address=input("Address: ")

s=student()
s.input_master()
print(s.adno)
print(s.name)
print(s.address)