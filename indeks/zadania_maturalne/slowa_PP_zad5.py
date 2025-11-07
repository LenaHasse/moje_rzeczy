with open('slowa.txt', 'r') as plik:
    lista_slowa=[i.strip() for i in plik]

    #5.1

    liczba_dlugosci={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
    for element in lista_slowa:
        dlugosc=len(element)
        liczba_dlugosci[dlugosc]+=1

    wyniki=open('wyniki_slowa_pp.txt','w')
    wyniki.write('5.1\n')
    for dlugosc in liczba_dlugosci:
        liczba_wierszy=liczba_dlugosci[dlugosc]
        wyniki.write(f'{dlugosc} {liczba_wierszy}\n')


    #5.2
    wyniki.write('5.2\n')

    with open('nowe.txt','r') as plik1:
        lista_nowe=[i.strip() for i in plik1]

        for i in lista_nowe:
            suma_nowe=0
            suma_odbicie=0
            for j in lista_slowa:
                if i==j:
                    suma_nowe+=1
                if j==i[::-1]:
                    suma_odbicie+=1
            wyniki.write(f'{i} {suma_nowe} {suma_odbicie}\n')



