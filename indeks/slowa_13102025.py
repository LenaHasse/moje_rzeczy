with open('slowa.txt','r') as plik1:
    slowatxt=plik1.readlines()
    lista_slowa=[i.strip for i in slowatxt]

print(lista)