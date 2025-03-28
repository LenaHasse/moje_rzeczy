#3.1
with open('liczby_przyklad.txt','r') as plik:
    lista_str=plik.read().split()
    lista_int=list(map(int,lista_str))
    print(lista_int)
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
        for i in range(2, x + 1):
            if x % i == 0:
                return False
        return True


    lista_pierwszych = []
    najwyzsza=max(lista_int)
    for i in range(0,int((najwyzsza**0.5)+1)):
        if czy_pierwsza(i)==True:
            lista_pierwszych.append(i)
    print(lista_pierwszych)

