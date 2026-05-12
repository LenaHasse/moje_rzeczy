with open('pociagi.txt','r')as plik:
    pociagi_start=[x.strip().split()for x in plik]

    pociagi=[]
    for i in range(1001,1051):
        wagony=[]
        for j in pociagi_start:
            if int(j[0])==i:
                wagony.append((int(j[0]),int(j[1])))
        if len(wagony)>=1:
            pociagi.append(wagony)

#zad1
zad1=0
zad1ton=0
def czy_pierwsza(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for i in pociagi_start:
    if czy_pierwsza(int(i[1])):
        zad1+=1
    if int(i[1])==41:
        zad1ton+=1

print(zad1)
print(zad1ton)
print()

#zad2
max_dlugosc=0
nr_pociagu=0
max_suma=0
for i in pociagi:
    if len(i)>max_dlugosc:
        max_dlugosc=len(i)
        nr_pociagu=i[0][0]
        suma=0
        for wagony in i:
            waga=int(wagony[1])
            suma+=waga
        max_suma=suma

print(nr_pociagu)
print(max_dlugosc)
print(max_suma)
print()

#zad3
zad3_nr_pociagu=0
powtarzajaca_nosnosc=0
ile_wagonow=0
for i in pociagi:
    najlepsza_dl=0
    najlepsza_nosnosc=0

    for idx in range(len(i)):
        nosnosc=i[idx][1]
        ile=0

        for j in range(len(i)):
            if i[j][1]==nosnosc:
                ile+=1

        if ile>najlepsza_dl:
            najlepsza_dl=ile
            najlepsza_nosnosc=nosnosc
    if najlepsza_dl>ile_wagonow:
        ile_wagonow=najlepsza_dl
        zad3_nr_pociagu=i[0][0]
        powtarzajaca_nosnosc=najlepsza_nosnosc

print(zad3_nr_pociagu)
print(powtarzajaca_nosnosc)
print(ile_wagonow)


