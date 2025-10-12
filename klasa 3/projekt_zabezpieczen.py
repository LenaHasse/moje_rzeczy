#zad1
def czujnik_ruchu(czujnik1,czujnik2):
    return czujnik1 or czujnik2

def drzwi_bezpieczne(zamek_glowny,zamek_awaryjny):
    return zamek_glowny and zamek_awaryjny

def wykryj_awarie(status_systemu):
    return not status_systemu

def alarm_przeciwpozarowy(czujnik_dymu,czujnik_temperatury):
    return (bool(czujnik_dymu)^bool(czujnik_temperatury))

#zad2

def wyswietl_stan_systemu():
    print(f"{'wejscie1':^10} {'wejscie2':^10} {'ruch':^10} {'drzwi':^10} {'awarie(wejscie1)':^10} {'pozar':^10}")
    print('-'*68)
    for a in range(2):
        for b in range(2):
            print(f'{a:^10} {b:^10} {czujnik_ruchu(a,b):^10} {drzwi_bezpieczne(a,b):^10} {int(wykryj_awarie(a)):^15} {int(alarm_przeciwpozarowy(a,b)):^11}')
    print('\n'*2)

#mam nadzieje ze dobrze zinterpetowalam zad2, bo nie bylam pewna do konca jak ta tabela ma wygladac
wyswietl_stan_systemu()

#zad3

def ALARM(wykryto_ruch, wykryto_wibracje,godziny_otwarcia):
    return (wykryto_ruch and wykryto_wibracje)^(not godziny_otwarcia)

def wykryj_wlamanie():
    print(f"{'Ruch':^10} {'Wibracje':^10} {'Otwarte':^10} {'ALARM':^10}")
    print(42*'-')
    for a in range(2):
        for b in range(2):
            for c in range(2):
                print(f'{a:^10} {b:^10} {c:^10} {int(ALARM(a,b,c)):^10}')
    print('\n'*2)

wykryj_wlamanie()
