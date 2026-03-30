from collections import Counter
def nwd_pierwszy(n):
    n_temp=n
    czynniki=[]
    if n<1:
        return 1
    if n==2:
        print('2 | 2')
    else:
        i=2
        while n>1:
            if n%i==0:
                czynniki.append(i)
                n//=i
                while n%i==0:
                    czynniki.append(i)
                    n//=i
            i+=1
        if not czynniki:
            czynniki.append(n_temp)

        wynik=Counter(czynniki)

        txt = ""
        for wartosc, ilosc  in wynik.items():
            if ilosc==1:
                txt += f'{wartosc}' +'*'
            else:
                txt += f'{wartosc}^{ilosc}' + "*"

        if txt[-1] == "*":
            txt = txt[:-1]
        print(f'{txt} | {max(czynniki)}')

t = int(input())
for i in range(t):
    k = int(input())
    nwd_pierwszy(k)

