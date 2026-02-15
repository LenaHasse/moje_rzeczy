with open('odbiorcy.txt','r')as plik:
    odbiorcy=[int(x) for x in plik]
    #zad2
    zad1=0
    for i in range(1,len(odbiorcy)):
        if i not in odbiorcy:
            zad1+=1
    print(zad1)

    #zad3
    pakiety=[]
    for i in range(len(odbiorcy)):
        pakiety.append(i+1)


    def rundy(lista):
        pakiet=list(lista)
        for i in range(len(odbiorcy)):
            lista[i]=pakiet[odbiorcy[i]-1]
        return lista

    nr_rundy=0
    warunek=True
    while warunek:
        temp=rundy(pakiety)
        nr_rundy+=1
        for i in range(len(temp)):
            if temp[i]== i+1:
                zad3=(nr_rundy,i+1)
                warunek=False
                break


    print(zad3)
    #zad4
    pakiety=[i+1 for i in range(len(odbiorcy))]
    slownik={}
    with open('wyniki4.txt','w')as wyniki:
        wyniki.write('4.2\n')
        wyniki.write(str(zad1))
        wyniki.write('\n4.3\n')
        wyniki.write(str(zad3))
        wyniki.write('\n4.4\n')
        for i in range(8):
            n=rundy(pakiety)
            if i==0 or i==1 or i==3 or i==7:
                for j in range(len(n)):
                    if n[j] in slownik:
                        slownik[n[j]]+=1
                    else:
                        slownik[n[j]]=1
                ile= max(slownik.values())
                wyniki.write(str(ile))
                wyniki.write(' ')
                slownik.clear()




