#3.1
with open('liczby_przyklad.txt','r') as plik:
    lista_str=plik.read().split()
    lista_int=list(map(int,lista_str))

    wynik=0
    ilosc_liczb=0

    for liczba in lista_int:
        if int(liczba**0.5)**2==liczba:
            ilosc_liczb+=1
            if wynik==0:
                wynik=liczba

    print(f"pierwsza liczba: {wynik}, są {ilosc_liczb} liczb/y, które są kwadratami")


    #3.2
    def czy_pierwsza(x):
        if x < 2:
            return False
        for i in range(2, x):
            if x % i == 0:
                return False
        return True


    lista_pierwszych = [i for i in range(2, int(max(lista_int)**0.5) + 1) if czy_pierwsza(i)]

    lista_liczb_podzielnych=[]

    for liczba in lista_int:
        podzielniki=sum(1 for p in lista_pierwszych if liczba%p==0)
        if podzielniki>=5:
            lista_liczb_podzielnych.append(liczba)

    print(list(lista_liczb_podzielnych))

    #3.3
    def roznica_cyfr_w_liczbie(liczba):
        lista=[int(i) for i in str(liczba)]

        lista_min=sorted(lista)
        lista_max=sorted(lista,reverse=True)

        liczba_min=int(''.join(map(str, lista_min)))
        liczba_max = int(''.join(map(str, lista_max)))
        return liczba_max-liczba_min
        
    def analizuj_roznice(lista):
        wyniki={'mniejsza':0,'wieksza':0,'rowna':0}
        for liczba in lista:
            roznica=roznica_cyfr_w_liczbie(liczba)
            if roznica<liczba:
                wyniki['mniejsza']+=1
            elif roznica>liczba:
                wyniki['wieksza']+=1
            else:
                wyniki["równa"] += 1

        return wyniki

    print(analizuj_roznice(lista_int))
