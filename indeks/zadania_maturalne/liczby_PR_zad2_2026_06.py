#2.1
def ciecia_liczb(k):
    a=0
    b=0
    temp_k=k
    dlugosc=0
    potega_10=10
    while temp_k>0:
        dlugosc+=1
        temp_k//=10

    polowa_dlugosci=dlugosc//2
    dzielnik=1
    for i in range(polowa_dlugosci):
        dzielnik*=10

    a=k//dzielnik

    b=k%dzielnik

    return a,b

#2.2
def nwd(a,b):
    if b==0:
        return a
    return nwd(b,a%b)

with open('liczby1.txt','r') as plik:
    lista=[int(x) for x in plik]
    polowicznie_wzglednie_pierwsza = 0
    for i in lista:
        a,b=ciecia_liczb(i)
        if nwd(a,b)==1:
            polowicznie_wzglednie_pierwsza+=1
    print(polowicznie_wzglednie_pierwsza)


