class a:
    b=10
    def access(self):
        print(b) # type: ignore

t=a()
n=a()

print(t.b)
print(n.b)       #static class