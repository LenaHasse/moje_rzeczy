import random

with open('poziom_latwy.txt', 'r') as plik1:
    hasla_latwe=plik1.read()

with open('poziom_trudny.txt', 'r') as plik3:
    hasla_trudne=plik3.read()

with open('poziom_sredni.txt', 'r') as plik2:
    hasla_srednie=plik2.read()

zgadniecie=True

lista_latwa= hasla_latwe.split()
lista_srednia=hasla_srednie.split()
lista_trudna=hasla_trudne.split()


haslo=str(lista_latwa[random.randint(0,len(lista_latwa))]).lower()
dlugosc_hasla=len(haslo) #ilosc liter w hasle
wynik=0             #zbieranie punktow za kazda litere, gdy wynik==dlugosci hasla to haslo zostalo zgadniete

zakryte_haslo=[]
for i in haslo:
    zakryte_haslo.append('_')

print(' '.join(zakryte_haslo))
print(haslo) #USUN POTEM
print('\n')

while dlugosc_hasla!=wynik:
    litera = str(input('Podaj litere: '))
    if litera in haslo:
        for i in range(len(haslo)):
            if haslo[i]==litera:
                zakryte_haslo[i]=litera
        wynik+=1
    else:
        print('Źle!')
    print(' '.join(zakryte_haslo))

print('Brawo, zgadles')
