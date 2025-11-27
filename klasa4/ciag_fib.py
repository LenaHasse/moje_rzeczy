def fib_rek(n):
    if n<=1:
        return n
    else:
        return fib_rek(n-1)+fib_rek(n-2)

print(fib_rek(5))

def fib_memoizacja(n,pamiec={}):
    if n in pamiec:
        return pamiec[n]
    if n<=1:
        return n

    wynik=fib_memoizacja(n-1,pamiec)+fib_memoizacja(n-2,pamiec)
    pamiec[n]=wynik
    return wynik

print(fib_memoizacja(5))
