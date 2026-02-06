def szybvkie_potegowanie(a,n):
    wynik=1
    while n>0:
        if n%2==1:
            wynik*=a
        a*=a
        n//=2
    return wynik

print(szybvkie_potegowanie(2,16))

def potega_mod(a,n,m):
    wynik=1
    a=a%m

    while n>0:
        if n%2==1:
            wynik=(wynik*a)%m
        a=(a*a)%m
        n//=2
    return wynik


print(potega_mod(2,100,1000))
print(287296%1000)