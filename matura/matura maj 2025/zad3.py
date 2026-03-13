with open('dron_przyklad.txt','r') as plik:
    temp=[x.split()for x in plik]

    lista=[]
    for i in temp:
        temp1=[]
        for j in i:
            temp1.append(int(j))
        lista.append(temp1)
    print(lista)

#zad1
def nwd(a,b):
    if b==0:
        return a
    return nwd(b,a%b)
ile1=0
for i in lista:
    temp=nwd(abs(i[0]),abs(i[1]))
    if temp>1:
        ile1+=1

print(ile1)

#zad2
#a
punkty=[]
x,y=0,0
punkty.append([x,y])
for dx,dy in lista:
    x+=dx
    y+=dy
    punkty.append([x,y])
print(punkty)
ile2=0
for dx,dy in punkty:
    if dx>0 and dx<5000 and dy>0 and dy<5000:
        ile2+=1

print(ile2)
#b
b=[]
for i in range(len(punkty)):
    for j in range(i+1,len(punkty)):
        sx=(punkty[i][0]+punkty[j][0])
        sy=(punkty[i][1]+punkty[j][1])

        if sx%2!=0 or sy%2!=0:
            continue

        x=sx//2
        y=sy//2

        if [x,y]in punkty:
            b.append(punkty[i])
            b.append([x,y])
            b.append(punkty[j])
            break
print(b)
#zad3
