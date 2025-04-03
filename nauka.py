#1
with open('tekst.txt','r') as plik:
    tekst=plik.read()

    def wielka_litera(tekst):
        suma=0
        for slowa in tekst.split():
            if slowa[0].isupper():
                suma+=1
        return suma

    print(wielka_litera(tekst))
    print()

    def najczestsze_slowo(tekst):
        slowa={}
        for slowo in tekst.split():
            if slowo in slowa:
                slowa[slowo]+=1
            else:
                slowa[slowo]=1
        najczestsze=max(slowa,key=slowa.get)
        return f"najczesciej wystepujace slowo: {najczestsze}, wystapilo {slowa[najczestsze]} razy"
    print(najczestsze_slowo(tekst))
    print()

    def zmianaliter(tekst):
        with open('zapisywanie.txt','w+') as f:
            f.write(tekst.lower())
        f.close()
#2
nominaly=[1,5,10,20,50]
def wydawanie_reszty(kwota,nominaly):
    wynik={}
    for nominal in sorted(nominaly,reverse=True):
        if kwota>=nominal:
            ilosc=kwota//nominal
            wynik[nominal]=ilosc
            kwota=kwota%nominal

    if kwota==0:
        return wynik
    else:
        return None

print(wydawanie_reszty(432,nominaly))

#3
plansza = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0]
]
def otaczanie(plansza):
    for x in range(len(plansza)):
        for y in range(len(plansza[x])):
            if x==0 or x==len(plansza)-1 or y==0 or y==len(plansza)-1:
                plansza[x][y]=1

def wolne_pola(plansza,x,y):
    kierunki=[(0,1),(1,0),(0,-1),(-1,0)]
    sasiedzi=[]
    for dx,dy in kierunki:
        nowy_x,nowy_y=x+dx,y+dy
        if 0<=nowy_x<len(plansza) and 0<=nowy_y<len(plansza[0]) and plansza[nowy_x][nowy_y]==0:
            sasiedzi.append((nowy_x,nowy_y))
    return sasiedzi
print(wolne_pola(plansza,0,0))