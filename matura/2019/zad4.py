with open('liczby_przyklad.txt','r')as plik:
    lista=[int(x) for x in plik]

def czy_pierwsza(n):
    if n<2:
        return False

    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

zad1=[]
for i in lista:
    if i>=100 and i<=5000 and czy_pierwsza(i):
        zad1.append(i)

print(zad1)

#zad2
zad2=[]
with open('pierwsze_przyklad.txt','r')as plik1:
    pierwsze=[x.strip() for x in plik1]
for i in pierwsze:
    if czy_pierwsza(int(i[::-1])):
        zad2.append(i)

print()
print(zad2)

#zad3
def waga(n):
    while len(n)>1:
        suma=0
        for cyfra in n:
            suma+=int(cyfra)
        n=str(suma)
    return int(n)
zad3=[]

for i in pierwsze:
    if waga(i)==1:
        zad3.append(i)

print(zad3)
