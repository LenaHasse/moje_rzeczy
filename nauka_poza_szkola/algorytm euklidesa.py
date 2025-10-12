def nwd_iteracyjnie(a,b):
    while b!=0:
        temp=b
        b=a%b
        a=temp
    return a

print(nwd_iteracyjnie(1701,3768))

def nwd_rekurencyjnie(a,b):
    if b==0:
        return a
    else:
        return nwd_iteracyjnie(b,a%b)

def nww(a,b):
    return int((a*b)/nwd_rekurencyjnie(a,b))


print(nww(3768,1701))

def skroculamek(licznik,mianownik):
    d=nwd_rekurencyjnie(licznik,mianownik)
    nowy_licznik=int(licznik/d)
    nowy_mianownik=int(mianownik/d)
    return nowy_licznik,nowy_mianownik

print(skroculamek(1701,3768))