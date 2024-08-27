class sequence_series:
    def fact(self,n):
        p=1
        i=1
        while (i<=n):
            p=p*i
            i=i+1

        return p
    
    def natural(self,n):
        p=0
        i=1
        while(i<=n):
            p=p+i
            i=i+1
        return p
    
r=sequence_series()
print(r.fact(5))
print(r.natural(5))