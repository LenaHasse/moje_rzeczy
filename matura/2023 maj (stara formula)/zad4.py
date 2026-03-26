with open('przyklad.txt','r')as plik:
    slowa=[x.strip()for x in plik]

#zad1
zad1=[]
for i in slowa:
    if i.count('w')==i.count('k'):
        zad1.append(i)

print(zad1)
#zad2
zad2=[0]*len(slowa)
for id, s  in enumerate(slowa):
    #a w k c j e
    wakacje=[s.count('a')//2, s.count('w'),s.count('k'),s.count('c'),s.count('j'),s.count('e')]
    liczba=min(wakacje)
    if liczba >=1:
        zad2[id]=liczba

print(zad2)

#zad3
def min_wykreslanie(slowo, target):
    i=0
    count=0
    for litera in slowo:
        if litera==target[i]:
            i+=1
            if i==len(target):
                count+=1
                i=0
    return len(slowo)-count*len(target) if count>0 else len(slowo)

wzorzec='wakacje'
zad3=[ min_wykreslanie(slowo, wzorzec) for slowo in slowa]

print(zad3)

