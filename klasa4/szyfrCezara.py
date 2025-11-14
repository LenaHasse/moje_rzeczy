def szyfrujCezara(tekst,przesuniecie):
    wynik=''
    for znak in tekst:
        if znak.isalpha():
            if znak.isupper():
                pozycja=ord(znak)-ord('A')
                nowa_pozycja=(pozycja + przesuniecie)%26
                nowy_znak=chr(nowa_pozycja+ord('A'))
                wynik+=nowy_znak
            else:
                pozycja = ord(znak) - ord('a')
                nowa_pozycja = (pozycja + przesuniecie) % 26
                nowy_znak = chr(nowa_pozycja + ord('a'))
                wynik += nowy_znak
        else:
            wynik+=znak
    return wynik

def deszyfruj_cezara(tekst,przesuniecie):
    return szyfrujCezara(tekst,-przesuniecie)
print(szyfrujCezara('AbcSDef',3))
