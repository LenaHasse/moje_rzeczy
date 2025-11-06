def szyfrujCezara(tekst,przesuniecie):
    wynik=''
    for znak in tekst:
        if znak.isupper():
            znak=ord(znak)
            znak+=5
            znak+=znak%26
            znak=chr(znak)
            wynik+=znak
        if znak.islower():
            znak = ord(znak)
            znak += 5
            znak+=znak%26
            znak = chr(znak)
            wynik += znak

    return wynik


print(szyfrujCezara('AbcSDef',3))
