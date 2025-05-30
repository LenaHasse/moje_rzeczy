def f(x,licznik=0):
    if not isinstance(x,int) and x<0:
        return ValueError,'Liczba musi byc calkowita i nieujemna'
    licznik += 1
    if x==0:
        return 0,licznik
    else:
        wynik,licznik=f(x//2,licznik)
        return 2+wynik,licznik
for i in range
