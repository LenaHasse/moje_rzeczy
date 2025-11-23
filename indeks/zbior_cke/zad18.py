def nwd(a,b):
    wynik=0
    while b!=0:
        r=a%b
        a=b
        b=r
        wynik+=1
    return a

a=nwd(121,nwd(330,nwd(990,nwd(1331,nwd(110,225)))))
lista=[36,24,72,150]
print(a)
def nwd_lista(lista):
    wynik=lista[0]
    for i in lista[1:]:
        wynik= nwd(wynik,i)
    return wynik
print(nwd_lista(lista))