tekst='ALGORYTM_PRZESTAWIENIOWY'
d=len(tekst)
n=1
while n**2<d:
    n+=1
if d<n**2:
    tekst+='_'*(n**2-d)
s=n**2

print(tekst)
print(d)
szyfr=''
zmienna=0
for i in range(n):
    zmienna=i
    while zmienna<d:
        szyfr+=tekst[zmienna]
        zmienna+=n

print(szyfr)