with open('liczby15.txt','r')as plik:
    liczby=[int(x) for x in plik]

#zad1
def czy_pierwsza(n):
    if n<=1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True

zad1=0
for i in liczby:
    if czy_pierwsza(i):
        zad1+=1

print(zad1)

#zad2
b_superpierwsze=[]
pierwsze=[]
for i in liczby:
    if czy_pierwsza(i):
        pierwsze.append(i)

for i in pierwsze:
    suma_cyfr=sum(int(x) for x in str(i))

    if czy_pierwsza(suma_cyfr):

        suma_bin=bin(i).count('1')

        if czy_pierwsza(suma_bin):
            b_superpierwsze.append(i)

print(sorted(b_superpierwsze))

#zad3
zad3=[]
for i in range(len(liczby)-1):
    for j in range(i+1,len(liczby)):
        if abs(liczby[i]-liczby[j])==2 and czy_pierwsza(liczby[i]) and czy_pierwsza(liczby[j]):
            zad3.append([liczby[i],liczby[j]])

print(zad3)
