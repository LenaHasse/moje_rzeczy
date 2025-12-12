with open('mecz_przyklad.txt','r') as plik:
    mecze=plik.read().strip()

    #zad1
    zad1=0
    for i in range(len(mecze)-1):
        if mecze[i]!=mecze[i+1]:
            zad1+=1
    #zad2
    wygranaA=0
    wygranaB=0
    kto_wygral=''
    wynik=''

    for i in mecze:
        if i=='A':
            wygranaA+=1
        elif i=='B':
            wygranaB+=1

        if wygranaA>=1000 and wygranaB+3<wygranaA:
            kto_wygral='A'
            wynik=f'{wygranaA}:{wygranaB}'
            break

        if wygranaB>=1000 and wygranaA+3<wygranaB:
            kto_wygral='B'
            wynik=f'{wygranaB}:{wygranaA}'
            break

    print(kto_wygral)
    print(wynik)

    #zad3
    ile_dobrych_pass=0
    najdluzsza_passa=0
    kto_najdluzsza_passa=''

    passa=1
    czyja_aktualna_passa=mecze[0]

    for i in range(1,len(mecze)):
        if czyja_aktualna_passa==mecze[i]:
            passa+=1

            if najdluzsza_passa<passa:
                najdluzsza_passa=passa
                kto_najdluzsza_passa=mecze[i]

        if czyja_aktualna_passa!=mecze[i]:
            if passa>=10:
                ile_dobrych_pass+=1
            passa=1
            czyja_aktualna_passa=mecze[i]

    print()

    print(ile_dobrych_pass)
    print(najdluzsza_passa)
    print(kto_najdluzsza_passa)




