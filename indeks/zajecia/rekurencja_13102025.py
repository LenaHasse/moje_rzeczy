import math
ile=0


def sum_of_digits(number:int):
    global ile
    ile+=1
    if number==0:
        return 0
    return number%10+sum_of_digits(number//10)

def gcd(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

def gcd_modulo(a,b):
    while b!=0:
        temp=a%b
        a=b
        b=temp
    return a

def euklides_odejmowanie(a,b):
    if a==b:
        return a
    else:
        return gcd(abs(a-b),b)

def euklides_modulo(a,b):
    if b==0:
        return a
    return euklides_modulo(b,a%b)

print(euklides_modulo(24,18))