with open('pesel.txt','r')as plik:
    pesele=[x.strip()for x in plik]
    print(pesele)

#zad1
kobiety=0

for i in pesele:
    if int(i[9])%2==0:
        kobiety+=1

mezczyzni=len(pesele)-kobiety
print(kobiety)
print(mezczyzni)
#zad2
def cyfra_kontrolna(n):
    pesel=n[0:10]
    waga=[1,3,7,9,1,3,7,9,1,3]
    suma=0
    for i in range(len(pesel)):
        liczba=int(pesel[i])
        iloczyn=int(str((liczba*waga[i]))[-1])
        suma+=iloczyn
    wynik1=int(str(suma)[-1])
    return 10-wynik1

zad2=[]
for i in pesele:
    if cyfra_kontrolna(i)!=int(i[-1]):
        zad2.append(i)

print(zad2)

#zad3
do18=0
do50=0
do100=0
powyzej100=0

def rok_ur(pesel):
    liczba=int(pesel[0:2])
    miesiac=int(pesel[2:4])
    if miesiac>12:
        rok=2000+liczba
    else:
        rok=1900+liczba
    return 2022-rok

# print(rok_ur('98070803628'))

for i in pesele:
    wiek=rok_ur(i)
    if wiek<=18:
        do18+=1
    elif wiek<=50 and wiek>=19:
        do50+=1
    elif wiek>=51 and wiek<=100:
        do100+=1
    else:
        powyzej100+=1

print(do18)
print(do50)
print(do100)
print(powyzej100)

