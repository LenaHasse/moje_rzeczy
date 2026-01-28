with open('ciagi.txt','r')as plik:
    ciagi=[x.strip() for x in plik]

    #zad1
    zad1=[]
    for i in ciagi:
        w1=0
        w0=0
        if len(i)%2==0:
            polowa=len(i)//2
            pierwsza_polowa=i[:polowa]
            druga_polowa=i[polowa:]
            if pierwsza_polowa==druga_polowa:
                zad1.append(i)

    print(zad1)
    print(len(zad1))

    #zad2
    zad2=[]
    for ciag in ciagi:
        if '11' not in ciag:
            zad2.append(ciag)
    print(zad2)
    print(len(zad2))

    #zad3
    zad3=0
    najmniejsza=float('inf')
    najwieksza=0
    dziesietne_ciagi=[]
    for i in ciagi:
        dziesietne_ciagi.append(int(i,2))
    def czy_pierwsza(n):
        if n<2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True

    for i in dziesietne_ciagi:
        for j in range(int(i**0.5)+1):
            if czy_pierwsza(j)==True and i%j==0:
                dzielnik=i/j
                if czy_pierwsza(dzielnik):
                    zad3+=1
                    if najwieksza<i:
                        najwieksza=i
                    if najmniejsza>i:
                        najmniejsza=i
    print(zad3)
    print(najmniejsza)
    print(najwieksza)


