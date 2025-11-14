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
