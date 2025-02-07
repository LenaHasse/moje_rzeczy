with open('sygnaly.txt','r') as plik:
    sygnaly=plik.readlines()

for i in range(39,len(sygnaly),40):
    tekst=sygnaly[i]
    print(tekst[9],end='')
print()

def liczba_liter(s):
    s=s.strip()
    return len(set(s.lower()))
zad2=max(sygnaly, key=liczba_liter)
print(zad2.strip(),liczba_liter(zad2))
print()


for linijka1 in sygnaly:
    linijka = linijka1[:-1]
    trafiona = True
    for i in range(len(linijka)):
        for j in range(i+1,len(linijka)):
            if abs(ord(linijka[i])-ord(linijka[j]))>10:
                trafiona=False
                break
    if trafiona==True:
        print(linijka)
