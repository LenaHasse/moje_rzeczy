
def kompresujRLE(tekst):
    if tekst=='':
        return ''
    wynik=''
    aktualny_znak=tekst[0]
    licznik=1
    for i in range(1,len(tekst)):
        if tekst[i]==aktualny_znak:
            licznik+=1
        else:
            wynik+=f'{licznik}{aktualny_znak}'
            aktualny_znak=tekst[i]
            licznik=1

    wynik+=f'{licznik}{aktualny_znak}'
    return wynik

def dekompresuj_RLE(skompresowany):
    wynik=''
    i=0

    while i<len(skompresowany):
        licznik=''
        liczby=[x for x in skompresowany if x.isdigit()]
        while i<len(skompresowany) and skompresowany[i].isdigit():
            licznik+=skompresowany[i]
            i+=1

        znak=skompresowany[i]
        wynik+=znak*int(licznik)
        i+=1
    return wynik


def wspolczynnikKompresji(oryginalny,skompresowany):
    return len(oryginalny)/len(skompresowany)


print(kompresujRLE('wwwwwiiiikkkkkkkiiippppppeeeeeddddiia'))
print(dekompresuj_RLE('5w4i7k3i6p5e4d2i1a'))

