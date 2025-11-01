#zad1
with open('mecz.txt','r') as plik:
    tekst=plik.read().strip()
    suma=0
    for i in range(1,len(tekst)):
        if tekst[i]!=tekst[i-1]:
            suma+=1
    wyniki=open('wyniki1.txt','w')

    wyniki.write('1\n')
    wyniki.write(str(suma))
    wyniki.write('\n')
    wyniki.write('\n')

    #zad2
    sumaA=0
    sumaB=0
    i=0
    while  i<len(tekst):
        if tekst[i]=='A':
            sumaA+=1
        if tekst[i]=='B':
            sumaB+=1

        if sumaA>=1000 and sumaA-sumaB>=3:
            break

        if sumaB>=1000 and sumaB-sumaA>=3:
            break

        i+=1

    wyniki_zad2=''

    if sumaA>sumaB:
        wyniki_zad2=f'A {sumaA} : {sumaB}'
    if sumaB>sumaA:
        wyniki_zad2=f'B {sumaA} : {sumaB}'

    wyniki.write('2\n')
    wyniki.write(wyniki_zad2)
    wyniki.write('\n')
    wyniki.write('\n')

    #zad3
    dlugosc_passy=1

    ilosc_pass=0
    team_najdluzsza_passa=''
    najdluzsza_passa=0
    poprzednia_wygrana=tekst[0]


    for i in range(1,len(tekst)):
        if tekst[i]==poprzednia_wygrana:
            dlugosc_passy+=1

        else:
            if dlugosc_passy >=10:
                ilosc_pass += 1

                if dlugosc_passy>najdluzsza_passa:
                    team_najdluzsza_passa=poprzednia_wygrana
                    najdluzsza_passa=dlugosc_passy

            dlugosc_passy=1
            poprzednia_wygrana=tekst[i]
    if dlugosc_passy>=10:
        ilosc_pass+=1

        if dlugosc_passy>najdluzsza_passa:
            najdluzsza_passa=dlugosc_passy
            team_najdluzsza_passa=tekst[i]

    wyniki.write('3\n')
    wyniki.write(f'{ilosc_pass} {team_najdluzsza_passa} {najdluzsza_passa}')
    wyniki.close()



