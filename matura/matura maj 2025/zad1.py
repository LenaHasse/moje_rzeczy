with open('symbole.txt','r')as plik:
    symbole=[x.strip()for x in plik]
    #zad1
    zad1=[]
    for i in symbole:
        if i==i[::-1]:
            zad1.append(i)
    print(zad1)
    print()

    #zad2
    zad2=[]
    for i in range(len(symbole)-2):
        for j in range(10):
            czy_kwadrat=True
            sprawdzamy=symbole[i][j]
            for di in range(3):
                for dj in range(3):
                    if symbole[i+di][j+dj]!=sprawdzamy:
                        czy_kwadrat=False
                        break
                if not czy_kwadrat:
                    break
            if czy_kwadrat:
                zad2.append((i+2,j+2))
    print(len(zad2))
    print(zad2[len(zad2)//2])
    print()

    #zad3
    nowa_lista=[]

    for i in symbole:
        slowo=''
        for j in i:
            if j=='o':
                slowo+='0'
            elif j=='+':
                slowo+='1'
            elif j=='*':
                slowo+='2'
        nowa_lista.append(slowo)

    def trojkowy_na_dziesietny(n):
        wynik=0
        for i in n:
            wynik= 3*wynik+int(i)
        return wynik

    max3_symbol=''
    max3=-1

    symbole_int=[]

    for i in nowa_lista:
        symbole_int.append(trojkowy_na_dziesietny(i))

    for idx,val in enumerate(symbole_int):
        if val>max3:
            max3=val
            max3_symbol=symbole[idx]
    print(max3_symbol)
    print(max3)
    print()

    #zad4
    zad4_int=sum(symbole_int)

    def dziesietny_na_trojkowy(n):
        if n==0:
            return '0'
        wynik=''
        while n>0:
            wynik+=str(n%3)
            n//=3
        return wynik[::-1]

    zad4_3=dziesietny_na_trojkowy(zad4_int)
    print(zad4_int)
    #print(zad4_3)
    wynik4=''
    for i in zad4_3:
        if i=="0":
            wynik4+='o'
        elif i=='1':
            wynik4+='+'
        elif i=='2':
            wynik4+='*'
    print(wynik4)