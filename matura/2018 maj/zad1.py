def algorytym(n):
    p=1
    q=n
    while p<q:
        s=(p+q)//2
        if s*s*s<n:
            p=s+1
        else:
            q=s
    return p

print(algorytym(28))
print(algorytym(64))
print(algorytym(80))

print(algorytym(10**3))
for i in range(10**3):
    if algorytym(i)==10:
        print(i)
        break