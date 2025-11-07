with open('pary.txt', 'r') as plik:
    lista_list=[list(x.strip().split()) for x in plik]
    lista_liczb=[int(i[0]) for i in lista_list]
    lista_slow=[i[1] for i in lista_list]

    wyniki=open('../wyniki4.txt', 'w')
    #zad1
    wyniki.write('4.1\n')
    def czy_pierwsza(n):
        if n<2:
            return False
        for i in range(2,n):
            if n%i==0:
                return False
        return True

    liczby_parzyste=[x for x in lista_liczb if x%2==0]
    for i in liczby_parzyste:
        wyniki.write(f'{i} ')
        for j in range(i):
            if czy_pierwsza(j):
                if czy_pierwsza(i-j):
                    wyniki.write(f'{j} {i-j}')
                    break
        wyniki.write('\n')
    wyniki.write('\n')
    #zad2
    wyniki.write('4.2\n')
    for i in lista_slow:
        max_suma_ciag=0
        max_ciag=''

        suma_ciag=0
        ciag=''

        for j in range(len(i)):
            if j==0:
                suma_ciag=1
                ciag=i[j]

            elif i[j]==i[j-1]:
                suma_ciag+=1
                ciag+=i[j]

            else:
                if suma_ciag>max_suma_ciag:
                    max_suma_ciag=suma_ciag
                    max_ciag=ciag

                suma_ciag=1
                ciag=i[j]
        if suma_ciag>max_suma_ciag:
            max_suma_ciag=suma_ciag
            max_ciag=ciag

        wyniki.write(f'{max_ciag} {max_suma_ciag}\n')
    wyniki.write('\n')


    #zad3
    lista_zad3=[]
    for i in range(len(lista_list)):
        if lista_liczb[i]==len(lista_slow[i]):
            lista_zad3.append(lista_list[i])

    najmniejsza=[]
    def czy_posortowane(x):
        return list(x)==sorted(x)

    for i in range(len(lista_zad3)):
        if (-(int(lista_zad3[i][0]))<int(lista_zad3[i-1][0])) or (-int((lista_zad3[i][0]))==int(lista_zad3[i-1][0]) and czy_posortowane(lista_zad3[i][1])==True):
            najmniejsza=lista_zad3[i]

    wyniki.write('4.3\n')
    wyniki.write(f'{najmniejsza[0]} \n')
    wyniki.write(f'{najmniejsza[1]}\n')

