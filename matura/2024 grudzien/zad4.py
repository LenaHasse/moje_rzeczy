with open('prostokaty_przyklad.txt','r')as plik:
    lista_temp=[x.split()for x in plik]
    prostokaty=[]
    for i in lista_temp:
        prostokaty.append([int(i[0]),int(i[1])])

    print(prostokaty)

#zad1
#1 wysokosc 2 szerokosc

najmniejsze_pole=float('inf')
najwieksze_pole=0

for i in prostokaty:
    pole=i[0]*i[1]
    if pole>najwieksze_pole:
        najwieksze_pole=pole
    if pole<najmniejsze_pole:
        najmniejsze_pole=pole

print(najmniejsze_pole)
print(najwieksze_pole)
print()

#zad2
poprzednia_wysokosc=prostokaty[0][0]
poprzednia_szerokosc=prostokaty[0][1]

dlugosc_ciagu=1

max_ciag=0
max_wysokosc=0
max_szerokosc=0

for i in range(1,len(prostokaty)):
    wysokosc,szerokosc=prostokaty[i]
    poprzednia_wysokosc,poprzednia_szerokosc = prostokaty[i-1]

    if (wysokosc>=poprzednia_wysokosc and
        szerokosc>=poprzednia_szerokosc):
        dlugosc_ciagu += 1

        if dlugosc_ciagu>max_ciag:
            max_ciag=dlugosc_ciagu
            max_wysokosc=wysokosc
            max_szerokosc=szerokosc
    else:
        dlugosc_ciagu=1


print(max_ciag)
print(max_wysokosc)
print(max_szerokosc)
