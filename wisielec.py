with open('poziom_latwy.txt', 'r') as plik1:
    hasla_latwe=plik1.read()

with open('poziom_trudny.txt', 'r') as plik3:
    hasla_trudne=plik3.read()

with open('poziom_sredni.txt', 'r') as plik2:
    hasla_srednie=plik2.read()


hasla_latwe.lower()
hasla_srednie.lower()
hasla_trudne.lower()

lista_latwa= hasla_latwe.split()
lista_srednia=hasla_srednie.split()
lista_trudna=hasla_trudne.split()

print(lista_srednia)