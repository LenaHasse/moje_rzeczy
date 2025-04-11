with open('entry_arr.txt','r') as plik:
    liczby=plik.read()
    lista_liczb=[int(i) for i in liczby.split()]
    lista_liczb.sort()

    macierz=[]
    lista=[]

    for a in lista_liczb:
        for b in lista_liczb[a:]:
            if b%a==0:
                lista.append(a)
                lista.append(b)
                print(lista)
        break
        macierz.append(lista)
        lista=[]
    print(macierz)
'''
    for a in lista_liczb:
        for  b in lista_liczb[a:]:
            for c in lista_liczb[b:]:
                for d in lista_liczb[c:]:
                    for e in lista_liczb[d:]:
                        lista.append(a)
                        if b%a==0:
                            lista.append(b)
                            if c%b==0:
                                lista.append(c)
                                if d%c==0:
                                    lista.append(d)
                                    if e%d==0:
                                        lista.append(e)
                        
'''
