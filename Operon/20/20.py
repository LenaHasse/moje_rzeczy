with open('wyrazy.txt','r')as plik:
    wyrazy=[x.strip()for x in plik]
    print(wyrazy)
with open('anagramy.txt','r')as plik1:
    temp=[x.strip()for x in plik1]
    anagramy=[]
    for i in temp:
        temp1=i.split()
        a,b=temp1[0],temp1[1]
        anagramy.append([a,b])
    print(anagramy)

#zad1
zad1=0
for i in anagramy:
    a=sorted(i[0])
    b=sorted(i[1])
    if a==b:
        zad1+=1

print(zad1)
print()

#zad2
zad2=[]

for a, b in anagramy:
    if sorted(a)==sorted(b):
        continue
    if len(a)!=len(b):
        continue

    target=sorted(a)
    znalezione=False
    for i in range(len(b)):
        for ch in (chr(x)for x in range(ord('A'), ord('Z')+1)):
            if ch==b[i]:
                continue
            nowy=list(b)
            nowy[i]=ch

            if sorted(nowy)==target:
                zad2.append([a,b,i+1,ch])
                znalezione=True
                break
        if znalezione:
            break

print(zad2)
print()
#zad3
target="bura"
# to ja mam tutaj sama je wygenerowac? bo funkcja moja nic nie generowala, nie ma takich

def generuj_kombinacje(n):
    if len(n)<=1:
        return [n]
    wynik=[]
    for i in range(len(n)):
        pierwsza=n[i]
        reszta=n[:i]+n[i+1:]

        for anagram in generuj_kombinacje(reszta):
            wynik.append(pierwsza+anagram)
    return wynik

#zad3 kontynuacja
for i in set(generuj_kombinacje('bura')):
    print(i)

print()
licznik=1
#nawet nie będę sprawdzać tego z odpowiedziami, ufam intuicji
for i in wyrazy:
    print(f'WYRAZ {licznik}')
    for x in set(generuj_kombinacje(i)):
        print(x)

