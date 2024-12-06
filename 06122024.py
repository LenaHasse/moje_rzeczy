with open('liczby_przyklad.txt','r') as liczby:
    czytanie=liczby.read()

lista_poczatkowa=czytanie.split()
lista_int=[int(x)-1 for x in lista_poczatkowa]

max_wartosc=max(lista_int)

lista_pierwsze=[]
lista_pierwsze.append(False)
lista_pierwsze.append(False)
def sito(n):
    lista_pierwsze = []
    lista_pierwsze.append(False)
    lista_pierwsze.append(False)
    for i in range(2, n+1):
        lista_pierwsze.append(True)
    for i in range(2,n+1):
        if lista_pierwsze[i]==True:
            j=i*2
            while j<=n:
                lista_pierwsze[j]=False
                j+=i
    return lista_pierwsze

cos=sito(10000)
wynik=0
for i in lista_int:
    if cos[i]==True:
        wynik+=1
print(wynik)
