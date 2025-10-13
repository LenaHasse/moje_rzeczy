with open('liczby.txt','r') as plik:
    tekst=plik.readlines()
    lista=[int(i.strip()) for i in tekst]
    lista2=[i.strip() for i in tekst]
#zad1
pierwsze=sorted(lista)
parzyste=[]
for i in pierwsze:
    if i%2==0:
        parzyste.append(i)
najwieksza=parzyste[len(parzyste)-1]
print(najwieksza)

#zad2
palindrom=[]
for i in lista2:
    if i==i[::-1]:
        palindrom.append(i)

print(palindrom)
#zad3
sumy_cyfr=[]
wieksze_od_30=[]
for i in lista2:
    suma=0
    for j in str(i):
        suma+=int(j)
    sumy_cyfr.append(suma)

for i in range(0,len(sumy_cyfr)):
    if sumy_cyfr[i]>30:
        wieksze_od_30.append(lista2[i])
wieksze_od_30_int=[int(i) for i in wieksze_od_30]

def suma_cyfr(liczba):
    suma = 0
    for x in (str(liczba)):
        suma += int(x)
    return suma

suma_wszystkich=0
for i in lista:
    suma_wszystkich+=suma_cyfr(i)
print(wieksze_od_30_int)
print(suma_wszystkich)
