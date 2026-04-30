with open('dane.txt','r')as plik:
    dane=[x.split('.')for x in plik]
    print(dane)
    print()

#zad1
zad1={}
for i in dane:
    rodzaj_przesylki=i[0][0:3]

    if rodzaj_przesylki not in zad1:
        zad1[rodzaj_przesylki]=1
    else:
        zad1[rodzaj_przesylki]+=1

najwiecej=0
max_rodzaj=''
for rodzaj, ile in zad1.items():
    if najwiecej<ile:
        najwiecej=ile
        max_rodzaj=rodzaj

print(najwiecej)
print(max_rodzaj)
print()

#zad2
from collections import Counter
imiona=[]
for i in dane:
    imie=i[1].upper()
    imiona.append(imie)

imiona_counter=Counter(imiona)
final_imiona=sorted(imiona_counter.items(),key=lambda x:x[1],reverse=True)
for imie, ile in final_imiona:
    print(f'{imie}:{ile}')
