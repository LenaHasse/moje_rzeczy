def znajdz_wzorzec(tekst, wzorzec):
    tekst=tekst.split()
    indeksy=[]
    for i in range(len(tekst)):
        if tekst[i]==wzorzec:
            indeksy.append(i)
    return indeksy

#to wyszukuje dobrze, ale jak pamietam Pan zrobił wersję gdzie chodzi o indeks pierwszej litery (?)
def znajdz_wzorzec2(tekst,wzorzec):
    indeksy=[]
    for i in range(len(tekst)-len(wzorzec)+1):
        if tekst[i:i+len(wzorzec)]==wzorzec:
            indeksy.append(i)

    return indeksy

#to zrobilam dwie










tekst = "Python is great. Python is everywhere!"
wzorzec = "Python"
print('wersja typowa lena')
print(znajdz_wzorzec(tekst, wzorzec))
print()

print('wersja nietypowa lena')
print(znajdz_wzorzec2(tekst, wzorzec))  # [0, 17] - wzorzec na pozycjach 0 i 17

tekst2 = "aaabaaabaaab"
wzorzec2 = "aab"
print('wersja typowa lena')
print(znajdz_wzorzec(tekst2, wzorzec2))  # [1, 5, 9]
print()
print('wersja nietypowa lena')
print(znajdz_wzorzec2(tekst2, wzorzec2))

print('wersja typowa lena')
print(znajdz_wzorzec("test", "xyz"))  # [] - nie znaleziono
print()
print('wersja nietypowa lena')
print(znajdz_wzorzec2("test", "xyz"))
