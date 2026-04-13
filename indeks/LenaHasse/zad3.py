with open('liczby.txt','r')as plik:
    lista=[int(x)for x in plik]


#zad1
zad1=list(set(lista))
wynik1=[]
def nwd(a,b):
    if b==0:
        return a
    return nwd(b,a%b)

for i in range(len(zad1)):
    if i+1<len(zad1):
        if nwd(zad1[i],zad1[i+1])==1:
            if zad1[i]>zad1[i+1]:
                krotka=(zad1[i+1],zad1[i])
            else:
                krotka=(zad1[i],zad1[i+1])
            if krotka not in wynik1:
                wynik1.append(krotka)
print(len(wynik1))


#zad2
zad2a=0
zad2b=[]
for i in range(len(lista)):
    if i+2<len(lista):
        if len(str(lista[i]))+len(str(lista[i+1]))==len(str(lista[i+2])):
            zad2a+=1
            if len(str(lista[i]))<len(str(lista[i+1])) and len(str(lista[i+1]))< len(str(lista[i+2])):
                zad2b.append([lista[i],lista[i+1],lista[i+2]])

print(zad2a)
print(zad2b)

#zad3

def czy_pierwsza(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

poprzednia=0
ciag=0
najdluzszy_c=0
pierwsza=0
ostatnia=0
for i in lista:
    if czy_pierwsza(i):
        if ciag==0:
            pierwsza=i
            ciag=1
            poprzednia=i
        if ciag>=1:
            if poprzednia<i:
                ciag+=1
                poprzednia=i
            else:
                ciag=1
                poprzednia=i
                pierwsza=i
    else:
        if ciag>najdluzszy_c:
            najdluzszy_c=ciag
            ostatnia=i

if ciag>najdluzszy_c:
    najdluzszy_c=ciag
    ostatnia=i

print()
print(najdluzszy_c)
print(pierwsza)
print(ostatnia)


with open('wyniki3.txt','w') as wyniki:
    wyniki.write('3.1\n')
    wyniki.write(str(len(wynik1)))
    wyniki.write('\n')
    wyniki.write('3.2\n')
    wyniki.write(str(zad2a))
    wyniki.write('\n')
    wyniki.write(str(zad2b))
    wyniki.write('\n')
    wyniki.write('3.3\n')
    wyniki.write(str(najdluzszy_c))
    wyniki.write('\n')
    wyniki.write(str(pierwsza))
    wyniki.write('\n')
    wyniki.write(str(ostatnia))




