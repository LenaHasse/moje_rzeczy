import math
tekst='kochanowski'
liczba=3
def szyfrowanie(n,dane):
    tablice=math.ceil(len(dane)/(n**2)) #ile jest tablic
    znaki=tablice*(n**2) #ile jest znakow (z iksami)
    brakujace_znaki=znaki-len(dane) #ile brakuje znakow do "pelnej" tablicy
    dane+=brakujace_znaki*'x'
    print(dane)
    for i in range(0,tablice+1):
        tablica=''
        for k in range(0,n):
            for j in range(k,n**2,n):
                tablica+=(dane[j])

    return(tablica)

print(szyfrowanie(liczba,tekst))
