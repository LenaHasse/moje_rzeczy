with open('59.txt','r') as plik:
    lista=[int(x) for x in plik]

    #zad1
    #przed panstwem najbardziej nieoptymalny program w zyciu lenki <3
    liczba_trzy_czynniki=0

    def czy_pierwsza(n):
        if n<2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True

    def rozklad(n):
        czynniki=[]
        for i in range(3,n+1):
            if n%i==0 and czy_pierwsza(i):
                if i not in czynniki:
                    czynniki.append(i)
        return czynniki

    for i in lista:
        if i % 2 != 0:
            if len(rozklad(i))==3:
                liczba_trzy_czynniki+=1

    print(liczba_trzy_czynniki)
  
