with open('liczby13.txt','r') as plik:
    lista=[int(x)for x in plik]
    print(lista)
    #zad1
    lista_bin=[bin(x)[2:] for x in lista]
    def licz_0_1(n):
        zera=0
        jedynki=0
        for i in n:
            if i=='0':
                zera+=1
            else:
                jedynki+=1
        return zera,jedynki
    ilosc01=[]
    for i in lista_bin:
        ilosc01.append(licz_0_1(i))
    print(ilosc01)
    takie_same=0
    for i in ilosc01:
        if i[0]==i[1]:
            takie_same+=1
    print(takie_same)

    #zad2

