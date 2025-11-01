with open('liczby.txt','r') as plik:
    lista=[int(x) for x in plik]
#zad2
    def czy_pierwsza(x):
        if x<1:
            return False
        else:
            for i in range(2,int(x**0.5)+1):
                if x%i==0:
                    return False
            return True
    suma=0
    for i in lista:
        if czy_pierwsza(i-1):
            suma+=1
    wyniki=open('wyniki3.txt','w')
    wyniki.write('2\n')
    wyniki.write(str(suma))
    wyniki.write('\n')
    wyniki.write('\n')
    #zad3
    def sito_erastotenesa(n):
        sito=[True]*(n+1)
        sito[1]=False
        for i in range(2,n+1):
            if sito[i]:
                j=i*i
                while j<=n:
                    sito[j]=False
                    j+=i
        return sito


    max_n=max(lista)
    sito=sito_erastotenesa(max_n)

    #najwieksza suma
    liczba_z_najwieksza=0
    najwieksza_suma=-1

    #najmniejsza suma
    liczba_z_najmniejsza=0
    najmniejsza_suma=float('inf')

    for N in lista:
        suma_rozkladow=0

        for i in range(2,N//2+1):
            if sito[i]:
                druga_liczba=N-i

                if sito[druga_liczba]:
                    suma_rozkladow+=1

        if suma_rozkladow >najwieksza_suma:
            najwieksza_suma=suma_rozkladow
            liczba_z_najwieksza=N

        if suma_rozkladow<najmniejsza_suma:
                najmniejsza_suma=suma_rozkladow
                liczba_z_najmniejsza=N

    wyniki.write('3\n')
    wyniki.write(f'{liczba_z_najwieksza} {najwieksza_suma} {liczba_z_najmniejsza} {najmniejsza_suma}\n')
    wyniki.write('\n')
    #zad4
    lista_w_szesnastkowym=[]
    for i in lista:
        lista_w_szesnastkowym.append(hex(i)[2:])
    slownik={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'A':0,'B':0,'C':0,'D':0,'E':0,'F':0}
    for i in lista_w_szesnastkowym:
        for j in i.upper():
            slownik[j]+=1

    wyniki.write('4\n')
    for klucz, wartosc in slownik.items():
        linia=f'{klucz}: {wartosc}\n'
        wyniki.write(linia)



