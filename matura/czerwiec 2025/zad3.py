with open('dane_przyklad.txt','r')as plik:
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
    lista_liczb=list(set(lista_liczb))
    print(lista_liczb)
    #zad1
    zad1=0
    for i in lista_liczb:
        if i[:2]=='50':
            zad1+=1
    print(zad1)

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
#zad3
zad3=[]
for i in lista_liczb:
    if len(i)==9 and i[0]=='5':
        zad3.append(i)

print(zad3)

#zad4
nr_telefonow=[x for x in lista_liczb if len(x)==9]
print(nr_telefonow)
for i in nr_telefonow:
    slownik={}
    for j in i:
