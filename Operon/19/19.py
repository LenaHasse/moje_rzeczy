with open('oddzialy.txt','r')as plik:
    lista_temp=[x.strip()for x in plik]

    oddzialy=[]
    for i in lista_temp:
        a,b=i.split()

        oddzialy.append((int(a),int(b)))

print(oddzialy)
print()
#zad1
straty=0
poza_zasiegiem=0
odleglosc=[]
for i in oddzialy:
    temp=(i[1]**2+i[0]**2)**0.5
    odleglosc.append(temp)

for i in odleglosc:
    if i<1 or i>20:
        poza_zasiegiem+=1
    elif i==1.0 or i==20.0:
        straty+=25
    else:
        straty+=100
print(straty)
print(poza_zasiegiem)
print()

#zad2
maksymalna_odleglosc=round(max(odleglosc)+0.001,3)
print(maksymalna_odleglosc)

#zad3
max_trafionych=0
for i in range(-20,20):
    for j in range(-20,20):
        trafione=0
        for x,y in oddzialy:
            d=((i-x)**2+(j-y)**2)**0.5
            if d==2:
                trafione+=25
            if d<2:
                trafione+=100
        if trafione>max_trafionych:
            max_trafionych=trafione
            zad3_w=(i,j)

print(max_trafionych)
print(zad3_w)
