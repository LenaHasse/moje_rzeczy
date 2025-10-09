def przestaw(n):
    r=n%100
    a=r//10
    b=r%10
    n=n//100
    if n>0:
        w=a+10*b+100*przestaw(n)
    else:
        if a>0:
            w=a+10*b
        else:
            w=b
    return w

def wlasny_len(n):
    k=0
    while n!=0:
        n=n//10
        k+=1
    return k
def przestaw2(n):
    potega = 10
    reszta=0
    if n>0:
        if wlasny_len(n)%2==0:
            n=n//10
            
