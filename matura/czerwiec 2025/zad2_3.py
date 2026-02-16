with open('liczby2_przyklad.txt','r')as plik2:
    liczby2=[int(x)for x in plik2]

def ciecia_zad3(k):
    d = 0
    stopien = 0
    kwadrat=k**2
    temp = kwadrat
    while temp > 0:
        temp //= 10
        d += 1

    for i in range(d-1):
        if kwadrat==0:
            break
        b = kwadrat % 10 ** i
        kwadrat //= 10 ** i
        a = kwadrat
        if (a+b)<=k:
            stopien+=1

    return stopien
max3=0
liczb3=0
for i in liczby2:
    kaprekar=ciecia_zad3(i)
    if kaprekar>max3:
        max3=kaprekar
        liczb3=i


print(max3)
print(liczb3)
print(ciecia_zad3(7746))
