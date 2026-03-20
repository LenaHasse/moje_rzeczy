def symuluj(zadania, strategia_s1, strategia_s2):
    biezace_zadania = sorted(list(zadania))

    czas_s1 = 0
    czas_s2 = 0

    while biezace_zadania:
        if czas_s1<=czas_s2:
            if strategia_s1==0:
                zadanie=biezace_zadania.pop(0)
            else:
                zadanie=biezace_zadania.pop()
            czas_s1+=zadanie
        else:
            if strategia_s2==0:
                zadanie=biezace_zadania.pop(0)
            else:
                zadanie=biezace_zadania.pop()
            czas_s2+=zadanie
    return max(czas_s1,czas_s2)

wszystkie_zadania=[]
with open('zadania_przyklad.txt', 'r') as plik:
    for linia in plik:
        dane=[int(x) for x in linia.strip().split()]
        wszystkie_zadania.append(dane[1:])

#0-min 1-max
strategie=[(0,0),(1,1),(1,0),(0,1)]

wyniki=[]
for zadania_do_obliczenia in wszystkie_zadania:
    min_czas=float('inf')

    for s1,s2 in strategie:
        czas=symuluj(zadania_do_obliczenia,s1,s2)

        if czas<min_czas:
            min_czas=czas
    wyniki.append(min_czas)

print(wyniki)