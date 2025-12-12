with open('liczby.txt','r') as plik:
    lista=[int(x.strip()) for x in plik]
    print(lista)

    #zad1
    mniejsze_niz_1000=[]
    for i in lista:
        if i<1000:
            mniejsze_niz_1000.append(i)
    print(len(mniejsze_niz_1000))

    dwie_ostatnie=[]
    dwie_ostatnie.append(mniejsze_niz_1000[len(mniejsze_niz_1000)-1])
    dwie_ostatnie.append(mniejsze_niz_1000[len(mniejsze_niz_1000)-2])

    print(dwie_ostatnie)

    #zad2
    def dzielniki(n):
        dzielniki=[]
        for i in range(1,n+1):
            if n%i==0: 
                dzielniki.append(i)
        return dzielniki



    for i in lista:
        if len(dzielniki(i))==18:
            print(i)
            print(dzielniki(i))

    #zad3
    def nwd(a,b):
        while b>0:
            a,b=b,a%b
        return a

    wzglednie_pierwsza_max=0
    for i in lista:
        warunek=True
        for j in lista:
            if i==j:
                continue

            if nwd(i,j)>1:
                warunek=False
                break
        if warunek and wzglednie_pierwsza_max<i:
            wzglednie_pierwsza_max=i


    print()
    print(wzglednie_pierwsza_max)




