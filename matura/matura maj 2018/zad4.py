with open('sygnaly.txt','r')as plik:
    sygnaly=[x.strip()for x in plik]
    print(sygnaly)
    #zad1
    zad1=''
    for i in range(39,len(sygnaly),40):
        zad1+=sygnaly[i][9]
    print(zad1)
    print()

    #zad2
    ile_roznych2=0
    slowo=''
    for i in sygnaly:
        slownik={}
        for j in i:
            if j not in slownik:
                slownik[j]=1
            else:
                slownik[j]+=1
        roznych=len(slownik)
        if roznych>ile_roznych2:
            ile_roznych2=roznych
            slowo=i

    print(slowo)
    print(ile_roznych2)
    print()

    #zad3
    max_odleglosc3=[]
    for i in sygnaly:
        odleglosc=0
        for j in range(len(i)-1):
            for k in range(j+1,len(i)):
                l1=ord(i[j])
                l2=ord(i[k])
                if abs(l1-l2)>odleglosc:
                    odleglosc=abs(l1-l2)
        if 10>=odleglosc:
            max_odleglosc3.append(i)

    print(max_odleglosc3)