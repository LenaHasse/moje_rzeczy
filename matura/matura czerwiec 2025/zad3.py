with open('dane.txt','r')as plik:
    czyt=plik.read()
    lista_liczb=[]
    temp=''
    for i in czyt:
        if i.isdigit():
            temp+=i
        else:
            if temp!='':
                lista_liczb.append(temp)
            temp=''
    if temp!='':
        lista_liczb.append(temp)

    lista_unikalne=list(set(lista_liczb))
    #zad1
    zad1=0
    for i in lista_unikalne:
        if i[:2]=='50':
            zad1+=1
    print(zad1)
    print()

    #zad2
    cyfry={}
    for i in lista_liczb:
        for j in i:
            if j not in cyfry:
                cyfry[j]=1
            else:
                cyfry[j]+=1

    cyfra2=''
    wystapienia2=0
    for cyfra, wystapienie in cyfry.items():
        if wystapienia2<wystapienie:
            wystapienia2=wystapienie
            cyfra2=cyfra

    print(cyfra2)
    print(wystapienia2)
    print()
#zad3
zad3=[]
for i in lista_liczb:
    if len(i)==9 and i[0]=='5':
        zad3.append(i)

print(zad3)
print(len(zad3))
print()

#zad4
zad4_odp=[]
zad4_najmniejsza=float('inf')
nr_telefonow=[x for x in lista_unikalne if len(x)==9]
for i in nr_telefonow:
    zad4=[]
    for j in i:
        if j not in zad4:
            zad4.append(j)
    if len(zad4)<zad4_najmniejsza:
        zad4_najmniejsza=len(zad4)
        zad4_odp=[i]
    if len(zad4)==zad4_najmniejsza:
        zad4_odp.append(i)
print(set(zad4_odp))
print(zad4_najmniejsza)

