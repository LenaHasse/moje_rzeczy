def dodawanie_cyfr(n):
    wynik=0
    while n>0:
        wynik+=n%10
        n//=10
    return wynik

print(dodawanie_cyfr(1234))