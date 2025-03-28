import time
nominaly = [1, 3,4]
nominaly.sort()
kwota = 6

def wydaj_reszte(kwota,nominaly):
    start=time.time()
    nominaly.reverse()
    lista=[]
    for nominal in nominaly:
        while kwota/nominal>=1:
            lista.append(nominal)
            kwota-=nominal
    stop=time.time()
    return lista, stop-start

#ale w sumie da sie ten program zrobic optymalniej?





wynik,roznica = wydaj_reszte(kwota, nominaly)
print(wynik)
print(roznica)
