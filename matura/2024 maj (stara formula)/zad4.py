with open('plansza_przyklad.txt','r')as plik:
    temp=[x.split()for x in plik]

    statki=[]
    for i in temp:
        lista_temp=[]
        for j in i:
            lista_temp.append(int(j))
        statki.append(lista_temp)

for i in statki:
    print(i)
wysokosc = len(statki)
szerokosc = len(statki[0]) if wysokosc > 0 else 0

#zad1
def pole(x,y):
    return 0 <= x < szerokosc and 0 <= y < wysokosc

def czy_jednomasztowiec(x,y):
    if statki[y][x]==1:
        return False
    for dy in [-1,0,1]:
        for dx in [-1,0,1]:
            if dx==0 and dy==0:
                continue
            if pole(x+dx,y+dy):
                if statki[y+dy][x+dx]==1:
                    return False
    return True

zad1=0
for y in range(wysokosc):
    for x in range(szerokosc):
        if czy_jednomasztowiec(x,y):
            zad1+=1

#zad2
def czy_jednomasztowiec_specjalny(x,y):
    for dy in [-1,0,1]:
        for dx in [-1,0,1]:
            if dx==0 and dy==0:
                continue
            if pole(x+dx,y+dy):
                if statki[y+dy][x+dx]==1:
                    return False
    return True
i=0
zad2=0


for y in range(wysokosc):
    for x in range(i,szerokosc):
        if (statki[y][x]==1 and
                statki[x][y]==1 and
                czy_jednomasztowiec_specjalny(x,y) and
                czy_jednomasztowiec_specjalny(y,x)):
            zad2+=1
    i+=1


print(zad2)




