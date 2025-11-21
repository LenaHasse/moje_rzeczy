with open('piksele.txt', 'r') as plik:
    lista=[x.split() for x in plik]
    lista_wierszy=[]
    for i in lista:
        lista_temp=[]
        for j in i:
            lista_temp.append(int(j))
        lista_wierszy.append(lista_temp)


    wyniki=open('wyniki6.txt', 'w')
    #zad1
    najmniejszy=float('inf')
    najwiekszy=0
    for i in lista_wierszy:
        for j in i:
            if int(j)>najwiekszy:
                najwiekszy=j
            if int(j)<najmniejszy:
                najmniejszy=j
    wyniki.write('6.1\n')
    wyniki.write(f'Najjasniejszy: {najwiekszy}\nnajciemniejszy: {najmniejszy}\n\n')

    #zad2
    liczba_wierszy_do_usuniecia=0
    for i in lista_wierszy:
        if i!=i[::-1]:
            liczba_wierszy_do_usuniecia+=1
    wyniki.write('6.2\n')
    wyniki.write(str(liczba_wierszy_do_usuniecia))
    wyniki.write('\n\n')

    #zad3
    kontrastujace=0
    W=200
    K=320
    for i in range(W):
        for j in range(K):

            val=lista_wierszy[i][j]
            kontrastuje=False

            if j-1>=0 and abs(val-lista_wierszy[i][j-1])>128:
                kontrastuje=True

            elif j+1<K and abs(val-lista_wierszy[i][j+1])>128:
                kontrastuje=True

            elif i-1>=0 and abs(val-lista_wierszy[i-1][j])>128:
                kontrastuje=True

            elif i+1<W and abs(val-lista_wierszy[i+1][j])>128:
                kontrastuje=True

            if kontrastuje:
                kontrastujace+=1
    print(kontrastujace)



    wyniki.write('6.3\n')
    wyniki.write(f'{kontrastujace}\n\n')

    #zad4
    najduzsza_passa=0

    for j in range(K):
        passa=1
        for i in range(1,W):
            if lista_wierszy[i-1][j]==lista_wierszy[i][j]:
                passa+=1
            else:
                if passa> najduzsza_passa:
                    najduzsza_passa = passa
                passa=1

        if passa>najduzsza_passa:
            najduzsza_passa = passa

    print(najduzsza_passa)

    wyniki.write('6.4\n')
    wyniki.write(f"{najduzsza_passa}\n")

    wyniki.close()



