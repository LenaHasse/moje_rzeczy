with open('liczby_przyklad.txt','r')as plik:
    liczby=[int(x)for x in plik]
    #zad1
    pierwsza=0
    zad1=[]

    for i in liczby:
        if (i**0.5).is_integer():
            zad1.append(i)
            if pierwsza==0:
                pierwsza=i
    print(pierwsza)
    print(len(zad1))
    #zad2
    def czy_pierwsza(n):
        if n<2:
            return False
        if n==2:
            return True
        if n%2==0:
            return False
        for i in range(3,int(n**0.5)+1,2):
            if n%i==0:
                return False
        return True

    zad2=[]
    for i in liczby:
        dzielniki=set()
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                if czy_pierwsza(j):
                    dzielniki.add(j)

                drugi_dzielnik=i//j
                if czy_pierwsza(drugi_dzielnik):
                    dzielniki.add(drugi_dzielnik)

        if len(dzielniki)>=5:
            zad2.append(i)

    print(zad2)

    #zad3
    mniejsza=0
    wieksza=0
    rowna=0
    liczby_str=[]
    for i in liczby:
        liczby_str.append(str(i))

    for i in liczby_str:
        temp=[]
        for j in i:
            temp.append(j)

        najmniejsza=sorted(temp)
        najwieksza=sorted(temp)
        najwieksza.reverse()
        l1=int(''.join(najmniejsza))
        l2=int(''.join(najwieksza))

        roznica=l2-l1
        if roznica>int(i):
            wieksza+=1
        if roznica<int(i):
            mniejsza+=1
        if roznica==int(i):
            rowna+=1

    print(rowna)
    print(mniejsza)
    print(wieksza)



