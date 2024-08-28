class student:
    a="ksr college of technology"
    def access(self):
        self.a="welcome"

print(student.a)
f=student() #non static object
m=student()

f.access()

print(f.a)
print(m.a)
