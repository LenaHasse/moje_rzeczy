def wyszukiwanieBinarne_iteracyjnie(tablica,szukana):
    tablica.sort()
    lewy=0
    prawy=len(tablica)-1
    porownania=0
    while lewy<=prawy:
        srodek=(lewy+prawy)//2
        porownania+=1
        if tablica[srodek]==szukana:
            return srodek,porownania
        if tablica[srodek]<szukana:
            lewy=srodek+1
        else:
            prawy=srodek-1

def wyszukiwanieBinarne_rekurencyjne(tablica,szukana,lewy,prawy,porownania=0):
    if lewy>prawy:
        return -1,porownania
    srodek=(lewy+prawy)//2
    porownania+=1
    if tablica[srodek]==szukana:
        return srodek,porownania
    if tablica[srodek]<szukana:
        return wyszukiwanieBinarne_rekurencyjne(tablica,szukana,srodek,prawy,porownania)
    else:
        return wyszukiwanieBinarne_rekurencyjne(tablica,szukana,lewy,srodek,porownania)




tablica = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
szukana = int(input("Podaj liczbę do znalezienia: "))

print(wyszukiwanieBinarne_iteracyjnie(tablica,szukana))
print(wyszukiwanieBinarne_rekurencyjne(tablica,szukana,0,len(tablica)+1))

