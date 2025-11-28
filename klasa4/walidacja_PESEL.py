import datetime
def walidacjaDlugosc(pesel):
    return len(pesel)==11


def walidujSumeKontrolna(pesel):
    wagi=[1,3,7,9,1,3,7,9,1,3]
    suma=0

    for i in range(10):
        suma+=wagi[i]*int(pesel[i])

    cyfra_kontrolna=(10-(suma%10))%10

    return cyfra_kontrolna==int(pesel[-1])


def pobierzDate(pesel):
    rok=int(pesel[0:2])
    miesiac=int(pesel[2:4])
    dzien=int(pesel[4:6])

    if 1<=miesiac<=12:
        wiek=1900
    elif 21<miesiac<=32:
        miesiac-=20
        wiek=2000

    elif 81<=miesiac <=92:
        miesiac-=80
        wiek=1800

    rok_urodzenia=rok+wiek

    return rok_urodzenia,miesiac,dzien

def pobierzPlec(pesel):
    if int(pesel[-2])%2==0:
        return 'kobieta'
    return 'mezczyzna'

def obliczWiek(rok_ur,miesiac_ur,dzien_ur):
    data_teraz=datetime.datetime.now()

    aktualny_rok=data_teraz.year
    aktualny_miesiac=data_teraz.month
    aktualny_dzien=data_teraz.day

    wiek=aktualny_rok-rok_ur
    if aktualny_miesiac<miesiac_ur or (aktualny_miesiac==miesiac_ur and aktualny_dzien<dzien_ur):
        wiek=wiek-1

    return wiek



print(pobierzDate('54031863149'))

print(walidujSumeKontrolna('54031863149'))

print(pobierzDate('54031863149'))
data,miesiac,dzien=pobierzDate('54031863149')

print(pobierzPlec('54031863149'))

print(obliczWiek(data,miesiac,dzien))


