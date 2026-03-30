with open('anagram.txt','r')as plik:
    lista=[x.split() for x in plik]
#a
lista1=[]
for i in lista:
    warunek=True
    d=len(i[0])
    for slowo in i:
        if len(slowo)!=d:
            warunek=False
            break
    if warunek:
        lista1.append(i)
print(lista1)

#b
zadb=[]
for i in lista:
    warunek=True
    test=[x for x in i[0]]
    test.sort()
    for j in range(1,len(i)):
        sprawdz=[x for x in i[j]]
        sprawdz.sort()
        if sprawdz!=test:
            warunek=False
            break
    if warunek:
        zadb.append(i)

print(zadb)



