with open('59.txt','r') as plik:
    lista=[int(x) for x in plik]

    #zad1
    #przed panstwem najbardziej nieoptymalny program w zyciu lenki
    # liczba_trzy_czynniki=0
    #
    # def czy_pierwsza(n):
    #     if n<2:
    #         return False
    #     for i in range(2,int(n**0.5)+1):
    #         if n%i==0:
    #             return False
    #     return True
    #
    # def rozklad(n):
    #     czynniki=[]
    #     for i in range(3,n+1):
    #         if n%i==0 and czy_pierwsza(i):
    #             if i not in czynniki:
    #                 czynniki.append(i)
    #     return czynniki
    #
    # for i in lista:
    #     if i % 2 != 0:
    #         if len(rozklad(i))==3:
    #             liczba_trzy_czynniki+=1

    # print(liczba_trzy_czynniki)

    def factor(number):
        if number%2==0:
            return False
        i=3
        diff_numbers=set()
        while i*i<=number:
            if number%i==0:
                diff_numbers.add(i)
                number//=i
            else:
                i+=2
        if number>1:
            diff_numbers.add(number)
        return len(diff_numbers)==3

    count1=0
    for number in lista:
        if factor(number):
            count1+=1

    print(count1)

    #4.2


    liczby_palindromy=0
    for i in lista:
        if str(i)==str(i)[::-1]:
            suma_cyfr=i+int(str(i)[::-1])
            if str(suma_cyfr)==str(suma_cyfr)[::-1]:
                liczby_palindromy+=1


    print(liczby_palindromy)
