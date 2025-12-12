#r>0 i min 5 wyrazów ciągu!!!
with open('ciagi.txt','r') as plik:
    lista_temp=[x.strip() for x in plik]

    liczba_wyrazow=[]
    ciagi=[]
    for i in range(len(lista_temp)):
        if i%2==0:
            liczba_wyrazow.append(int(lista_temp[i]))
        else:
            ciagi.append(lista_temp[i])

    print(liczba_wyrazow)
    for i in range(len(ciagi)):
        ciagi[i]=ciagi[i].split()
    for ciag in ciagi:
        for element in range(len(ciag)):
            ciag[element]=int(ciag[element])

    print(ciagi)
    print()

    #zad1
    ile_arytm=0
    najwieksza_roznica=0
    for ciag in ciagi:
        potencjalna_roznica=ciag[1]-ciag[0]
        czy_arytm=True
        for indeks in range(len(ciag)-1):
            if ciag[indeks+1]-ciag[indeks]!=potencjalna_roznica:
                czy_arytm=False
                break

        if czy_arytm:
            ile_arytm+=1
            if najwieksza_roznica<potencjalna_roznica:
                najwieksza_roznica=potencjalna_roznica
    print(najwieksza_roznica)
    print(ile_arytm)
    print()

    #zad2
    zad2=[]
    for ciag in ciagi:
        najwiekszy_szescian=-1
        for liczba in ciag:
            pierwiastek=round(liczba**(1/3))
            if pierwiastek**3==liczba:
                if najwiekszy_szescian<liczba:
                    najwiekszy_szescian=liczba
        if najwiekszy_szescian!=-1:
            zad2.append(najwiekszy_szescian)
    print(zad2)
    print()
    #zad3
    with open('bledne.txt','r')as plik1:
        lista_temp = [x.strip() for x in plik1]

        liczba_wyrazow_bledne = []
        ciagi_bledne = []
        for i in range(len(lista_temp)):
            if i % 2 == 0:
                liczba_wyrazow_bledne.append(int(lista_temp[i]))
            else:
                ciagi_bledne.append(lista_temp[i])

        print(liczba_wyrazow_bledne)
        for i in range(len(ciagi_bledne)):
            ciagi_bledne[i] = ciagi_bledne[i].split()
        for ciag in ciagi_bledne:
            for element in range(len(ciag)):
                ciag[element] = int(ciag[element])

        print(ciagi_bledne)
        print()

        zad3=[]
        for ciag in ciagi_bledne:
            roznice={}
            for indeks in range(len(ciag)-1):
                roznica=ciag[indeks+1]-ciag[indeks]
                if roznica not in roznice:
                    roznice[roznica]=1
                else:
                    roznice[roznica]+=1
            prawidlowa_roznica=max(roznice, key=roznice.get)
            if ciag[1]-ciag[0]!=prawidlowa_roznica:
                zad3.append(ciag[0])
                continue

            for i in range(1,len(ciag)-1):
                if ciag[i+1]-ciag[i]!=prawidlowa_roznica:
                    zad3.append(ciag[i+1])
                    break
        print(zad3)





