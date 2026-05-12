L=259
def dec2bcd(n):
    w=0
    while n>0:
        cyfra=n%10
        n//=10

        bity=0
        while bity <4:
            w+=(cyfra%2)
            cyfra//=2
            bity+=1

    return w

print(dec2bcd(L))