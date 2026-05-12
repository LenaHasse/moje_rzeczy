with open('dane_przyklad.txt','r') as plik:
    dane=[int(x) for x in plik]

#zad1
def czy_pierwsza(n):
    if n<2:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True

najmniejsza1=float('inf')
najwieksza1=0
zad1=0

for i in dane:
    if czy_pierwsza(i):
        zad1+=1
        if najwieksza1<i:
            najwieksza1=i
        if najmniejsza1>i:
            najmniejsza1=i
print('4.1')
print(najmniejsza1)
print(najwieksza1)
print(zad1)
print()

#zad2
def czy_palindromiczna(n):
    binarna=bin(n)[2:]
    if binarna[0]=='0':
        return False
    else:
        if binarna==binarna[::-1]:
            return True
    return False

def czy_prawie_palindromiczna(n):
    binarna = bin(n)[2:]
    if binarna[0] == 0:
        return False
    else:
        ilosc_zer_na_koncu=0
        licznik=-1
        warunek=True
        while warunek:
            if binarna[licznik]=='0':
                ilosc_zer_na_koncu+=1
            else:
                warunek=False
                break
            licznik-=1
        nowa_binarna='0'*ilosc_zer_na_koncu+binarna

        if nowa_binarna==nowa_binarna[::-1]:
            return True
    return False

palindromy=0
prawie_palindromy=0
for i in dane:
    if czy_palindromiczna(i):
        palindromy+=1
    elif czy_prawie_palindromiczna(i):
        prawie_palindromy+=1
print('4.2')
print(palindromy+prawie_palindromy)
print()

#zad2
lista=[]
for i in dane:
    temp=[]
    for j in str(i):
        temp.append(int(j))
    temp=list(set(temp))
    temp=sorted(temp)
    lista.append(tuple(temp))
from collections import Counter
x=Counter(lista)

pary=0
for value in x.values():
    pary+= value * (value - 1) // 2

print(pary)