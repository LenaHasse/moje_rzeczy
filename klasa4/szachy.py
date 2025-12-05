from dataclasses import replace

with open('szachy_przyklad.txt','r') as plik:
    tekst=plik.readlines()
    plansze=[]
    for i in range(0,len(tekst),9):
        pojedyncza=[]
        for j in range(8):
            pojedyncza.append(tekst[j+i].strip())
        plansze.append(pojedyncza)

    #zad1
    ile_plansz=0
    najwiecej_kolumn=0


    #zad1

    for i in range(len(plansze)):
        plansza_ma_puste=False
        ile_kolumn = 0
        for wiersz in range(8):
            kolumna = 0
            for indeks in range(8):
                if plansze[i][indeks][wiersz]=='.':
                    kolumna+=1

            if kolumna==8:
                ile_kolumn+=1
                plansza_ma_puste=True

                if ile_kolumn>najwiecej_kolumn:
                    najwiecej_kolumn=ile_kolumn

        if plansza_ma_puste:
            ile_plansz+=1

    print(ile_plansz)
    print(najwiecej_kolumn)

    print()


    #zad2
    ile_rownowaga=0
    najmniejsza_rownowaga=float('inf')

    for i in range(len(plansze)):
        ile_czarnych=0
        ile_bialych=0

        for wiersz in range(8):

            for indeks in range(8):

                if plansze[i][wiersz][indeks].isupper():
                    ile_bialych+=1
                if plansze[i][wiersz][indeks].islower():
                    ile_czarnych+=1

        if ile_czarnych==ile_bialych:
            ile_rownowaga+=1
            if najmniejsza_rownowaga>ile_czarnych:
                najmniejsza_rownowaga=ile_czarnych+ile_bialych

    print(ile_rownowaga)
    print(najmniejsza_rownowaga)


    #zad3
    #sprawdzanie wierszy
    def szachowanie_wiersze(plansze):
        for plansza in range(len(plansze)):


            for wiersz in range(8):
                pojedynczy_wiersz=plansze[plansza][wiersz].replace('.','')
                pojedynczy_wiersz=list(set(pojedynczy_wiersz))

                for i in range(len(pojedynczy_wiersz)):
                    if pojedynczy_wiersz[i]=='W':
                        if i>0 and pojedynczy_wiersz[i-1]=='k':
                            return True
                        if i<(len(pojedynczy_wiersz)-1) and pojedynczy_wiersz[i+1]=='k':
                            return True

                    if pojedynczy_wiersz[i]=='w':
                        if i>0 and pojedynczy_wiersz[i-1]=='K':
                            return True
                        if i<(len(pojedynczy_wiersz)-1) and pojedynczy_wiersz[i+1]=='K':
                            return True

                    if pojedynczy_wiersz[i]=='k':
                        if i>0 and pojedynczy_wiersz[i-1]=='W':
                            return True
                        if i<(len(pojedynczy_wiersz)-1) and pojedynczy_wiersz[i+1]=='W':
                            return True

                    if pojedynczy_wiersz[i]=='K':
                        if i>0 and pojedynczy_wiersz[i-1]=='W':
                            return True
                        if i<(len(pojedynczy_wiersz)-1) and pojedynczy_wiersz[i+1]=='W':
                            return True


    szachowanie_wiersze(plansze)
    #sprawdzanie kolumn
    for plansza in range(len(plansze)):

        for wiersz in range(8):
            for indeks in range(8):
                pojedyncza_kolumna = plansze[plansza][wiersz].replace('.', '')
                pojedyncza_kolumna = list(set(pojedyncza_kolumna))







