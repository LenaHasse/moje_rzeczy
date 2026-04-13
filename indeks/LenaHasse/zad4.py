
def zamiana(liczba):
    global ile
    tekst='0.'
    k=1
    temp=liczba
    while liczba!=0:
        k=k*2
        temp=liczba-1/k
        if temp>=0:
            liczba=liczba-1/k
            tekst+='1'
            temp=liczba
        else:
            tekst+='0'
    return tekst

print(zamiana(0.38816411))