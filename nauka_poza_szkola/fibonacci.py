def Fibonacci_rek(n):
    if n<=1:
        return n
    else:
        return Fibonacci_rek(n-1)+Fibonacci_rek(n-2)


print(Fibonacci_rek(5))

def fib_it(n):
    if n<=1:
        return n
    a=0
    b=1
    for i in range(2,n+1):
        a,b=b,a+b
    return b

print(fib_it(5))

def fib_pamiec(n,pamiec={}):
    if n in pamiec:
        return pamiec[n]
    if n<=1:
        return n
    else:
        pamiec[n]=fib_pamiec(n-1,pamiec)+fib_pamiec(n-2,pamiec)
        return pamiec[n]

print(fib_pamiec(5))


