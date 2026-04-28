with open('liczby16.txt','r')as plik:
    liczby=[int(x)for x in plik]

#zad1
zad1=[]
def nwd(a,b):
    if b==0:
        return a
    return nwd(b,a%b)
for i in range(len(liczby)-1):
    for j in range(i+1,len(liczby)):
        if nwd(liczby[i],liczby[j])==1:
            a,b=sorted((liczby[i],liczby[j]))
            zad1.append((a,b))
unikalne=set(zad1)
print(len(unikalne))

#zzad2
zad2=[]
def dzielniki(n):
    wynik=[1,n]
    for i in range(2,n):
        if n%i==0:
            wynik.append(i)
    return wynik


for i in liczby:
    if len(dzielniki(i))==9:
        zad2.append(i)

print(zad2)

#zad3
zad3=[]
def dzielniki2(n):
    wynik=[1]
    for i in range(2,n):
        if n%i==0:
            wynik.append(i)
    return wynik

for i in liczby:
    temp=sum(dzielniki2(i))
    if temp==i:
        zad3.append(i)

print(zad3)


