def skroc(n):
    if len(str(n))>1:
        return str(n)[:-1]
    else:
        return 0


def dopisz(n):
    if n==0:
        return 0
    return n*10

def ostatnia(n):
    return int(str(n)[-1])
wynik=0
def f(a,b):
    global wynik
    if b==0:
        return 0
    k=ostatnia(b)
    w=f(a,skroc(b))
    w=dopisz(w)
    while k>0:
        w=w+a
        wynik += 1
        k=k-1
    return w


print(f(2024,1234))
print(wynik)
