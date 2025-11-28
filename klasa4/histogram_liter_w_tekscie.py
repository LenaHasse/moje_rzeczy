import math
def zlicz_litery(tekst):
    licznik={}
    for i in tekst:
        if i.isalpha():
            i=i.lower()
            if i in licznik:
                licznik[i]+=1
            else:
                licznik[i]=1

    return licznik

def rysujHistogram(licznik,maksymalna_dlugosc=50):
    if len(licznik)==0:
        return 0
    max_wystapien=max(licznik.values())


    for litera in sorted(licznik.keys()):
        ile=licznik[litera]
        dlugosc_paska=math.ceil((ile/max_wystapien)*maksymalna_dlugosc)

        gwiazdki='*'*dlugosc_paska
        print(litera,':',gwiazdki,'(',ile,')')


print(zlicz_litery('AGgmepL'))
rysujHistogram(zlicz_litery('AGgmepL'))

def znajdzEkstrema(licznik):
    max_wystapien=max(licznik.values())
    min_wystapien = min(licznik.values())
    return min_wystapien,max_wystapien

def obliczStatystyki(licznik):
    calkowitaLiczbaLiter=0
    for ilosc in licznik.values():
        calkowitaLiczbaLiter+=ilosc
    unikalne=[]
    for znak,ilosc in licznik.items():
        if ilosc==1:
            unikalne.append(znak)


    return calkowitaLiczbaLiter,unikalne

print(obliczStatystyki(zlicz_litery('AGgmepL')))