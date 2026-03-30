with open('pesel.txt','r')as plik:
    lista=[x.strip()for x in plik]
    print(lista)

#a
zad_a=0
for i in lista:
    if i[2:4]=='12':
        zad_a+=1

print(zad_a)

#b
zad_b=0

for i in lista:
    if int(i[9])%2==0:
        zad_b+=1

print(zad_b)

#c
slownik_c={}
for i in lista:
    rok=i[0:2]
    if rok not in slownik_c:
        slownik_c[rok]=1
    else:
        slownik_c[rok]+=1
max_c=0
rok_c=''
for rok, ilosc in slownik_c.items():
    if ilosc>max_c:
        max_c=ilosc
        rok_c=rok
print(rok_c)

#d
def cyfra_kontrolna(pesel):
    pesel_bez=pesel[:-1]
    ostatnia=int(pesel[-1])
    lista_pesel=[int(x) for x in pesel_bez]

    wagi=[1,3,7,9,1,3,7,9,1,3]
    suma=0

    for i in range(len(lista_pesel)):
        suma+=lista_pesel[i]*wagi[i]
    if suma%10==0:
        return ostatnia==0
    else:
        return 10-suma%10==ostatnia

zad_d=[]
for i in lista:
    if cyfra_kontrolna(i)==False:
        zad_d.append(i)
zad_d.sort()

print(zad_d)






