with open('liczby_przyklad.txt','r')as plik:
    lista=[x.split() for x in plik]
    liczby=[]
    for i in lista:
        temp=[]
        for j in i:
            temp.append(int(j))
        liczby.append(temp)

print(liczby)
print()
#zad1
zad1=0
warunek=True
for i in liczby[0]:
    warunek=False
    for j in liczby[1]:
        if j%i==0:
            warunek=True
    if warunek:
        zad1+=1

print(zad1)
print()

#zad2
zad2=sorted(liczby[0])
print(zad2[100])
print()
#zad3

zad3=[]
mozliwe_liczby=list(liczby[0])
licznik_mozliwych={}
for i in mozliwe_liczby:
    if i not in licznik_mozliwych:
        licznik_mozliwych[i]=1
    else:
        licznik_mozliwych[i]+=1

def rozklad(n):
    wynik=[]
    for i in mozliwe_liczby:
        if n%i==0:
            wynik.append(i)
            n//=i
            while n%i==0:
                n//=i
                wynik.append(i)
    return wynik
warunek=True
from collections import Counter
for i in liczby[1]:
    warunek=True
    rozklady=rozklad(i)
    licznik=Counter(rozklady)
    if len(rozklady)>1:
        for j in licznik:
            if licznik_mozliwych[j]<licznik[j]:
                warunek=False
                break
        if warunek:
            zad3.append(i)




print(zad3)
