cena_bulki = 0.10
suma = cena_bulki*3
zaplacono = 0.30

print(f"Do zapłaty: {suma} zł")
print(f"Zapłacono:  {zaplacono} zł")

if suma == zaplacono:
    print("OK - kwota się zgadza")
else:
    print("BŁĄD - kwota się nie zgadza!")