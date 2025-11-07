with open('trojki.txt','r')as plik:
    lista=[list(map(int, x.split())) for x in plik]
    print(lista)
    wyniki=open('wyniki4','w')

    #4.1
    suma=0
    def is_sorted(lista):
        return lista==sorted(lista)
    for i in lista:
        if is_sorted(i):
            suma+=1
    wyniki.write('4.1\n')
    wyniki.write(str(suma))
    wyniki.write('\n')

    #4.2
    suma2=0
    def nwd(a,b):
        if b==0:
            return a
        return nwd(b,a%b)


    for i in lista:
        suma2+=nwd(nwd(i[0],i[1]),i[2])

    wyniki.write('4.2\n')
    wyniki.write(str(suma2))
    wyniki.write('\n')

    #4.3
    suma35=0
    maksymalna_suma=0
    ile_maksymalnych=0

    def suma_cyfr(n):
        wynik=0
        while n>0:
            wynik+=n%10
            n//=10
        return wynik

    for i in lista:
        wiersz=suma_cyfr(i[0])+suma_cyfr(i[1])+suma_cyfr(i[2])
        if wiersz==35:
            suma35+=1
        if wiersz>maksymalna_suma:
            ile_maksymalnych=1
            maksymalna_suma=wiersz
        elif wiersz==maksymalna_suma:
            ile_maksymalnych+=1

    print(f'W {suma35} wierszach suma cyfr jest rowna 35 \nMaksymalna suma jest {maksymalna_suma}, ktora wystapila {ile_maksymalnych} razy')



