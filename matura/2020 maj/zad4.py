with open('pary.txt','r')as plik:
    lista=[x.strip() for x in plik]

    pary=[]

    for i in lista:
        temp=i.split()
        liczba=int(temp[0])
        slowo=temp[1]
        pary.append([liczba,slowo])

#zad1
def czy_pierwsza(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
zad1=[]
zad1_final=[]
for j in pary:
    liczba=j[0]
    if liczba>4 and liczba%2==0:
        for i in range(1,liczba):
            if czy_pierwsza(i):
                roznica=liczba-i
                if czy_pierwsza(roznica):
                    zad1.append([liczba,i,roznica])
                    break


print(zad1)

#zad2
slowa=[]
zad2=[]
for i in pary:
    slowa.append(i[1])

for slowo in slowa:
    max_dlugosc=1
    dlugosc=1
    slowo_temp=slowo[0]
    max_slowo=slowo[0]
    poprzedni=slowo[0]

    for i in slowo[1:]:
        if i==poprzedni:
            slowo_temp+=i
            dlugosc+=1
        else:
            if dlugosc>max_dlugosc:
                max_dlugosc=dlugosc
                max_slowo=slowo_temp
            slowo_temp=i
            poprzedni=i
            dlugosc=1
    zad2.append([max_slowo,max_dlugosc])

print(zad2)

#zad3
najmniejsza=None
for liczba, slowo in pary:

    if liczba==len(slowo):
        if (najmniejsza is None
            or liczba<najmniejsza[0]
            or (liczba==najmniejsza[0] and slowo<najmniejsza[1])):
            najmniejsza=[liczba,slowo]


print(najmniejsza)
