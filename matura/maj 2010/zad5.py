with open('pesel.txt', 'r')as plik:
    lista=[x.strip()for x in plik]
lista=[i[:11] for i in lista if len(i)>=11 and i[:11].isdigit()]
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
    if len(pesel)!=11 or not pesel.isdigit():
        return False

    wagi=[1,3,7,9,1,3,7,9,1,3]
    suma=sum(int(pesel[i])*wagi[i]for i in range(10))

    kontrolna=(10-(suma%10))%10

    return kontrolna==int(pesel[10])

zad_d=[]
for i in lista:
    if cyfra_kontrolna(i)==False:
        zad_d.append(i)
zad_d.sort()

for i in zad_d:
    print(i)





