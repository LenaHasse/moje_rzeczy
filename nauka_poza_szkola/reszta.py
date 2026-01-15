def binary_search_it(tablica, szukana):
    lewy=0
    prawy=len(tablica)-1
    while lewy<=prawy:
        srodek=(lewy+prawy)//2
        if tablica[srodek]==szukana:
            return srodek
        if tablica[srodek]<szukana:
            lewy=srodek+1
        else:
            prawy=srodek-1
    return -1

tablica = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
szukana = 5
print(binary_search_it(tablica,szukana))

def binary_search_rek(tablica,szukana,lewy,prawy):
    if lewy>prawy:
        return -1

    srodek=(lewy+prawy)//2
    if tablica[srodek]==szukana:
        return srodek
    if tablica[srodek]<szukana:
        return binary_search_rek(tablica,szukana,srodek+1,prawy)
    if tablica[srodek]>szukana:
        return binary_search_rek(tablica,szukana,lewy,srodek-1)

print(binary_search_rek(tablica,szukana,0,len(tablica)-1))