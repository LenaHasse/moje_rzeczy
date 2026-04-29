from collections import Counter
with open('wyrazy.txt','r')as plik:
    wyrazy=[x.strip()for x in plik]
    print(wyrazy)
with open('anagramy.txt','r')as plik1:
    temp=[x.strip()for x in plik1]
    anagramy=[]
    for i in temp:
        temp1=i.split()
        a,b=temp1[0],temp1[1]
        anagramy.append([a,b])
    print(anagramy)

#zad1
zad1=0
for i in anagramy:
    a=sorted(i[0])
    b=sorted(i[1])
    if a==b:
        zad1+=1

print(zad1)
print()

#zad2
zad2=[]
# def ile_roznic(a,b):
#     return sum(1 for x,y in zip(a,b)if x!=y)
# def niepasujace(a,b):
#     return[(b[i],i)for i in range(len(a))if a[i]!=b[i]]
# for i in anagramy:
#     s1,s2=i[0],i[1]
#     if sorted(s1)!=sorted(s2):
#         if ile_roznic(s1,s2)==1:
#             zad2.append([s1,s2,niepasujace(s1,s2)])
# print(zad2)
for s1,s2 in anagramy:
    if sorted(s1)==sorted(s2):
        continue
    c1=Counter(s1)
    c2=Counter(s2)

    roznice=0
    litera_do_wstawienia=None
    litera_do_usuniecia=None

    for lit in c1:
        if c1[lit]!=c2[lit]
            roznice+=abs()