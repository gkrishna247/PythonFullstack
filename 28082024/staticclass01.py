class student:
    college="ksr college of technology"
    def access(self):
        self.adno=input("Adno: ")
        self.name=input("Name: ")

f=student() #non static object
m=student()

f.access()
m.access()

print("Ad.no: ",f.adno)
print("Name: ",f.name)
print("CollegeName: ",f.college)
print("Ad.no: ",m.adno)
print("Name: ",m.name)
print("CollegeName: ",m.college)
