def walidacjaDlugosc(pesel):
    if len(pesel)!=11:
        return False

def walidujSumeKontrolna(pesel):
    wagi=[1,3,7,9,1,3,7,9,1,3]
    suma=0

    for i in range(9):
        liczba=int(pesel[i])
        suma+=wagi[i]*liczba

    cyfra_kontrolna=10-(suma%10)

    return cyfra_kontrolna==pesel[len(pesel)-1],cyfra_kontrolna

print(walidujSumeKontrolna('91012100000'))


