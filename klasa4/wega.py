with open('sygnaly.txt','r') as plik:
    lista=[x.strip() for x in plik]

    #zad1
    przeslanie=''
    for i in range(39,len(lista),40):
        w=lista[i]
        przeslanie+=w[9]

    print(przeslanie)

    #zad2
    najdluzsze_slowo=''
    dlugosc=0

    lista_liter=[]
    for i in lista:
        lista_liter = []
        for j in i:
            if j not in lista_liter:
                lista_liter.append(j)

        lista_liter=list(set(lista_liter))

        if len(lista_liter)>dlugosc:
            najdluzsze_slowo=i
            dlugosc=len(lista_liter)

    print(najdluzsze_slowo)
    print(dlugosc)


    #zad3
    spelniajace=[]
    for i in lista:
        slowo_str = i
        slowo=[]
        for j in i:
            slowo.append(ord(j))

        sorted(slowo)
        slowo=list(set(slowo))
        if abs(slowo[0]-slowo[-1])<=10:
            spelniajace.append(slowo_str)
    print(spelniajace)





