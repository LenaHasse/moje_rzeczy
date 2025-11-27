def wydajReszte(kwota,nominaly):
    nominaly.sort()
    nominaly.reverse()
    wynik={}
    for nominal in nominaly:
        if kwota>=nominal:
            ile_monet=kwota//nominal
            wynik[nominal]=ile_monet
            kwota=kwota%nominal

    return wynik

def sprawdzPoprawnosc(wynik,kwota):
    suma=0
    for nominal,ilosc in wynik.items():
        suma+=nominal*ilosc

    return suma==kwota

def liczIloscMonet(wynik):
    ilosc_monet=0
    for nominal, ilosc in wynik.items():
        ilosc_monet+=ilosc
    return ilosc_monet



nominaly = [500, 200, 100, 50, 20, 10, 5, 2, 1]
kwota=int(input('Kwota do wydania (w groszach) '))

print(wydajReszte(kwota,nominaly))
print(sprawdzPoprawnosc(wydajReszte(kwota,nominaly),kwota))
print(liczIloscMonet(wydajReszte(kwota,nominaly)))
