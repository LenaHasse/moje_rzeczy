
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
    def ile_szachow(krol_symbol,wieza_symbol):
        ile_szachow=0
        for plansza in plansze:
            czy_szachuje=False
            for wiersz in range(0,8):
                for kolumna in range(0,8):
                    if plansza[wiersz][kolumna]==krol_symbol:
                        wiersz_w_gore=wiersz-1
                        wiersz_w_dol=wiersz+1
                        kolumna_w_prawo=kolumna+1
                        kolumna_w_lewo=kolumna-1

                        while wiersz_w_gore>=0:
                            if plansza[wiersz_w_gore][kolumna]==wieza_symbol:
                                czy_szachuje=True
                                break
                            elif plansza[wiersz_w_gore][kolumna]!='.':
                                break
                            wiersz_w_gore-=1

                        while wiersz_w_dol<=7:
                            if plansza[wiersz_w_dol][kolumna]==wieza_symbol:
                                czy_szachuje=True
                                break
                            elif plansza[wiersz_w_dol][kolumna]!='.':
                                break
                            wiersz_w_dol+=1

                        while kolumna_w_prawo<=7:
                            if plansza[wiersz][kolumna_w_prawo]==wieza_symbol:
                                czy_szachuje=True
                                break
                            elif plansza[wiersz][kolumna_w_prawo]!='.':
                                break
                            kolumna_w_prawo+=1

                        while kolumna_w_lewo>=7:
                            if plansza[wiersz][kolumna_w_lewo]==wieza_symbol:
                                czy_szachuje=True
                                break
                            elif plansza[wiersz][kolumna_w_lewo]!='.':
                                break
                            kolumna_w_lewo+=1
            if czy_szachuje:
                ile_szachow+=1
        return ile_szachow



    print()
    print(ile_szachow('K',"w"))
    print(ile_szachow('k','W'))








