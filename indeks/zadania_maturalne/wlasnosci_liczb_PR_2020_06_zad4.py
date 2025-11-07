with open('dane_przyklad.txt','r') as plik:
    lista=[int(i) for i in plik]

    #4.1

    def czy_pierwsza(n):
        if n<2:
            return False
        for i in range(2,int(n**0.5)):
            if n%i==0:
                return False
        return True

    ile_pierwszych=0
    najmniejsza_pierwsza=float('inf')
    najwieksza_pierwsza=0
    for i in lista:
        if czy_pierwsza(i):
            ile_pierwszych+=1
            if i>najwieksza_pierwsza:
                najwieksza_pierwsza=i
            if i<najmniejsza_pierwsza:
                najmniejsza_pierwsza=i

    wyniki=open('wyniki4.txt','w')
    wyniki.write('4.1\n')
    wyniki.write(f'Liczba liczb pierwszych: {ile_pierwszych}\n Najwieksza liczba: {najwieksza_pierwsza}\n Najmniejsza liczba: {najmniejsza_pierwsza}\n')

    #4.2
    suma_palindromow=0
    lista_bin=[bin(i)[2:] for i in lista]

    for i in lista_bin:
        znaleziona=False

        if i==i[::-1]:
            suma_palindromow+=1
            znaleziona=True

        if not znaleziona:
            test=i

            for j in range(1,len(i)+1):
                test=f'0{test}'
                if test==test[::-1]:
                    suma_palindromow+=1
    print(suma_palindromow)

    wyniki.write('4.2\n')
    wyniki.write(f'{suma_palindromow}\n')

    #4.3
    def posortowane_cyfry(n):
        return ''.join(sorted(set(str(n))))
    grupy={}

    for liczba in lista:
        posortowany_ciag=posortowane_cyfry(liczba)
        if posortowany_ciag not in grupy:
            grupy[posortowany_ciag]=0
        grupy[posortowany_ciag]+=1

    wynik=0

    for k in grupy.values():
        if k>=2:
            wynik+=k*(k-1)//2

    print(wynik)