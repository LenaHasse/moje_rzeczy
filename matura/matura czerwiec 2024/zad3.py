with open('slowa.txt', 'r')as plik:
    lista=[x.strip()for x in plik]

    #zad1
    zad1=0
    for slowo in lista:
        for i in range(1,len(slowo)-1):
            if slowo[i-1]=="k" and slowo[i+1]=='t':
                zad1+=1
    print(zad1)
    #zad2
    #cezar (śmiech przez łzy)
    def ROT13(n):
        wynik=''
        for litera in n:
            kod=(ord(litera)-ord('a')+13)%26+ord('a')
            wynik+=chr(kod)
        return wynik
    zad2=0

    for slowo in lista:
        temp=ROT13(slowo)
        if slowo==temp[::-1]:
            zad2+=1
    print(zad2)
    #zad3
    zad3=[]
    for slowo in lista:
        polowa=len(slowo)/2
        slownik={}
        for litera in slowo:
            if litera not in slownik:
                slownik[litera]=1
            else:
                slownik[litera]+=1
        max_temp=max(slownik.values())
        if max_temp>=polowa:
            zad3.append(slowo)

    print(zad3)
with open('wyniki3.txt', 'w')as wyniki:
    wyniki.write("3.1\n")
    wyniki.write(str(zad1))
    wyniki.write('\n')
    wyniki.write("3.2\n")
    wyniki.write(str(zad2))
    wyniki.write('\n3.3')
    for i in zad3:
        wyniki.write('\n')
        wyniki.write(i)


