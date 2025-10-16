def znajdz_wzorzec(tekst,wzorzec):
    pozycje=[]
    lista_tekst=tekst.split()
    lista_tekst_strip=[i.strip() for i in lista_tekst]

    for i in range(0,len(lista_tekst_strip)):
            if lista_tekst_strip[i]==wzorzec:
                pozycje.append(i)
    return pozycje

# print(znajdz_wzorzec('Ala ma kota a kot ma Ale','ma'))


def znajdz_wzorzec2(tekst,wzorzec):
    pozycje=[]
    n=len(tekst)
    m=len(wzorzec)
    for i in range(0,n-m+1):
        dopasowano=True
        for j in range(0,m):
            if tekst[i+j]!=wzorzec[j]:
               dopasowano=False
               break

        if dopasowano:
            pozycje.append(i)
    return pozycje

print(znajdz_wzorzec2('Ala ma kota a kot ma Ale','ma'))

def pokaz_kontekst(tekst, pozycja,dlugosc_wzorca,ile_znakow=20):
    poczatek=tekst[pozycja]
    koniec=tekst
