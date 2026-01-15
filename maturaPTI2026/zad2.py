with open('zadania_przyklad.txt','r')as plik:
    lista=[x.strip()for x in plik]

    listazad2=[]
    for i in lista:
        listazad2.append(i.split())

    for i in range(len(listazad2)):
        listazad2[i].pop(0)
        for j in range(len(listazad2[i])):
            listazad2[i][j]=int(listazad2[i][j])
    print(listazad2)

    czas_serwer1=0
    czas_serwer2=0
    czas_ogolny=0
    najkrotszy_czas=float('inf')
    lista_najkrotszych=[]

    #0 min 1 maks
    strategie=[(0,1),(1,0),(0,0),(1,1)]
    for i in range(len(listazad2)):
        najkrotszy_czas = float('inf')
        for strategia in strategie:
            for j in range(len(listazad2[i])):

                if strategia==(0,1):
                    if czas_serwer1<=czas_ogolny:
                        czas_serwer1+=listazad2[i][j]
                        if czas_serwer2<=czas_ogolny:
                            czas_serwer1 += listazad2[i][-j]
                    elif czas_serwer2<=czas_ogolny:
                        czas_serwer2 += listazad2[i][-j]

                    elif czas_serwer1<czas_serwer2:
                        czas_ogolny=czas_serwer1
                    elif czas_serwer2<czas_serwer1:
                        czas_ogolny=czas_serwer2

                if strategia == (0, 0):
                    if czas_serwer1 <= czas_ogolny:
                        czas_serwer1 += listazad2[i][j]
                        j+=1
                        if czas_serwer2 <= czas_ogolny:
                            czas_serwer1 += listazad2[i][j]
                    elif czas_serwer2<=czas_ogolny:
                        czas_serwer2 += listazad2[i][j]

                    elif czas_serwer1 < czas_serwer2:
                        czas_ogolny = czas_serwer2
                    elif czas_serwer2 < czas_serwer1:
                        czas_ogolny = czas_serwer2

                if strategia == (1, 0):
                    if czas_serwer1 <= czas_ogolny:
                        czas_serwer1 += listazad2[i][-j]
                        if czas_serwer2 <= czas_ogolny:
                            czas_serwer1 += listazad2[i][j]

                    elif czas_serwer2<=czas_ogolny:
                        czas_serwer2 += listazad2[i][j]

                    elif czas_serwer1 < czas_serwer2:
                        czas_ogolny = czas_serwer2
                    elif czas_serwer2 < czas_serwer1:
                        czas_ogolny = czas_serwer2


                if strategia == (1, 1):
                    if czas_serwer1 <= czas_ogolny:
                        czas_serwer1 += listazad2[i][-j]
                        j+=1
                        if czas_serwer2 <= czas_ogolny:
                            czas_serwer1 += listazad2[i][j]
                    elif czas_serwer2<=czas_ogolny:
                        czas_serwer2 += listazad2[i][-j]

                    elif czas_serwer1 < czas_serwer2:
                        czas_ogolny = czas_serwer2
                    elif czas_serwer2 < czas_serwer1:
                        czas_ogolny = czas_serwer2

            print(czas_ogolny)

            if czas_ogolny<najkrotszy_czas:
                najkrotszy_czas=czas_ogolny
            czas_ogolny = 0

        lista_najkrotszych.append(najkrotszy_czas)

    print(lista_najkrotszych)









