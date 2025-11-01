with open('pary.txt','r') as plik:
    pary=[list(map(int,x.split())) for x in plik if x.strip()]
    wynik=[]
    wyniki=open('wyniki2.txt','w')
    #po jednym zwrocie mozna dostac sie tylko do 2^n lub do 2^n-1
    for i in pary:
        a,b=i[0],i[1]
        kopia_b=b
        while a<b:
            b=b//2
        if b==a:
            wynik.append(i)
    for i in wynik:
        wyniki.write(f'{i[0]} {i[1]}\n')

    wyniki.close()


