with open('zegar_binarny.txt','r')as plik:
    zegar_binarny=[x.strip().split()for x in plik]
#zad1
def bin2dec(n):
    bin=[int(x)for x in n]
    dec=0
    bit=8
    for i in range(4):
        dec=dec+bin[i]*bit
        bit//=2
    return dec

dziesietne=[]
for i in zegar_binarny:
    godzina=[]
    for j in i:
        godzina.append(bin2dec(j))
    dziesietne.append(godzina)
zad1_wiersze=[]
zad1=0
for i in range(len(dziesietne)):
    godzina=dziesietne[i]
    if godzina==[1,7,2,2,1,4]:
        zad1+=1
        zad1_wiersze.append(i+1)
print('2.4')
print(zad1)
for i in zad1_wiersze:
    print(i,end=' ')
print()
print('2.5')
#zad2
zad2=[]
for i in zegar_binarny:
    if i[2]==i[4] and i[3]==i[5]:
        zad2.append(i)
for i in zad2:
    for j in i:
        print(j,end=' ')
    print()