#zad1
with open('liczby.txt', 'r') as plik:
    lista=[int(x) for x in plik]

    najwieksza=0
    for i in lista:
        if i%2==0:
            if i>najwieksza:
                najwieksza=i

    wyniki=open('wyniki5.txt','w')
    wyniki.write('5.1\n')
    wyniki.write(str(najwieksza))
    wyniki.write('\n')
    #zad2
    wyniki.write('5.2\n')
    palindromy=[]
    for i in lista:
        if str(i)==str(i)[::-1]:
            wyniki.write(str(i))
            wyniki.write('\n')

    #zad3
    wyniki.write('5.3\n')
    def suma_cyfr(n):
        sum=0
        while n>0:
            sum+=n%10
            n//=10
        return sum

    for i in lista:
        if suma_cyfr(i)>30:
            wyniki.write(str(i))
            wyniki.write('\n')

    suma_wszystkich=0
    for i in lista:
        suma_wszystkich+=suma_cyfr(i)

    wyniki.write(f'Suma wszystkich: {suma_wszystkich}')
    wyniki.close()


