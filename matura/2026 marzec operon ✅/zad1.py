nominaly=[500,200,100,50,20,10,5,2,1]
def reszta(kwota,k=0):
    if kwota <=0:
        return 0
    x=kwota//nominaly[k]
    kwota=kwota-(x*nominaly[k])
    return x+reszta(kwota,k+1)

print(reszta(869))
def reszta2(kwota):
    wynik=0
    for i in nominaly:
        if kwota<=0:
            break
        wynik+=kwota//i
        kwota=kwota-(kwota//i)*i
        while kwota//i>=1:
            wynik += kwota // i
            kwota = kwota - (kwota // i) * i
    return wynik

print(reszta2(869))

