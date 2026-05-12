a=[1,0,1,1,1,0,1,0,1,0]
liczba_zer=0
l=1
p=len(a)
while l<=p:
    s=(l+p)//2
    if a[s]==1:
        p=s-1
    else:
        liczba_zer=liczba_zer+s-l+1
        l=s+1

print(liczba_zer)