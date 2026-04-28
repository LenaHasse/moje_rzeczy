with open('oddzialy.txt','r')as plik:
    lista_temp=[x.strip()for x in plik]

    oddzialy=[]
    for i in lista_temp:
        a,b=i.split()

        oddzialy.append((int(a),int(b)))

print(oddzialy)
#zad1
