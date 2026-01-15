def SzyfrujCezara(tekst,przesuniecie):
    wynik=''
    for znak in tekst:
        if znak.isalpha():
            if znak.isupper():
                pozycja=ord(znak)-ord('A')
                nowa_pozycja=(pozycja+przesuniecie)%26
                wynik+=chr(nowa_pozycja+ord('A'))
            if znak.islower():
                pozycja=ord(znak)-ord('a')
                nowa_pozycja=(pozycja+przesuniecie)%26
                wynik+=chr(nowa_pozycja+ord('a'))
        else:
            wynik+=znak
    return wynik
print(SzyfrujCezara('X t5yZ',3))
