with open('liczby14.txt','r') as plik:
    lista=[int(x) for x in plik]
    print(lista)

a,b=0,1
max_z_listy=max(lista)
lista_fib=set()
while a<=max_z_listy:
    lista_fib.add(a)
    a,b=b,a+b

zad1=[x for x in lista if x in lista_fib]

print(len(zad1))

#zad2
fib=[]
a,b=0,1

while a<=max_z_listy+3:
    fib.append(a)
    a,b=b,b+a
fib_set=set(fib)

kat1=[]
kat2=[]
kat3=[]
posortowane=sorted(lista)
i=0
for x in posortowane:
    if x in fib_set:
        continue

    while i+1<len(fib) and fib[i+1]<=x:
        i+=1

    lewy=fib[i]
    prawy=fib[i+1] if i+1<len(fib) else 10**18
    d=min(x-lewy,prawy-x)

    if d==1:
        kat1.append(x)
    elif d==2:
        kat2.append(x)
    elif d==3:
        kat3.append(x)

print(kat1)
print(kat2)
print(kat3)


#zad3
def czy_pierwsza(n):
    if n<=1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
zad3=[x for x in zad1 if czy_pierwsza(x)]

print(zad3)
