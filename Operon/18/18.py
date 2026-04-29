with open('trzyliczby.txt','r')as plik:
    lista_temp=[x.strip()for x in plik]
    trzyliczby=[]
    for i in lista_temp:
        a,b,c=i.split()
        trzyliczby.append([a,b,c])
print(trzyliczby)

from collections import Counter

def znajdz_system(a,b,c):
    wszystkie=a+b+c
    min_baza=max(2,max(int(ch,16)for ch in wszystkie)+1)
    for baza in range(min_baza,17):
        if int(a,baza)+int(b,baza)==int(c,baza):
            return baza

zestawy=[]
for a,b,c in trzyliczby:
    baza=znajdz_system(a,b,c)
    zestawy.append((a,b,c,baza))
licznik_baz=Counter(baza for _,_,_,baza in zestawy)
for baza in sorted(licznik_baz):
    print(f'baza {baza}: {licznik_baz[baza]} zestawów')

#zad2
najmniejsza=float('inf')
najwieksza=0
for a,b,c,baza in zestawy:
    for liczba in (a,b,c):
        wartosc=int(liczba,baza)
        if wartosc<najmniejsza:
            najmniejsza=wartosc
        if wartosc> najwieksza:
            najwieksza=wartosc

print(najmniejsza)
print(najwieksza)

#zad3

znak_counter=Counter()
znaki=0
for a,b,c,baza in zestawy:
    for liczba in (a,b,c):
        znak_counter.update(liczba)
        znaki+=len(liczba)

for znak, ile in znak_counter.most_common():
    procent=round(ile/znaki*100,2) if znaki>0 else 0
    print(f"'{znak}': {ile} ({procent}%)")