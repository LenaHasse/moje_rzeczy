with open('teksty.txt','r')as plik:
    teksty=[x.strip()for x in plik]

with open('wzorce.txt','r')as plik1:
    wzorce=[x.strip()for x in plik1]

#zad1
wszystkie_lac=0
jedna_lit=0
max_powt=0
wyraz_1=''
for i in teksty:
    zbior=[]
    slownik={}
    warunek=True
    for litera in i:
        if litera not in zbior:
            zbior.append(litera)
            if litera not in slownik:
                slownik[litera]=1
        else:
            slownik[litera]+=1
    for wartosc in slownik.values():
        if wartosc!=1:
            warunek=False
        if wartosc>max_powt:
            max_powt=wartosc
            wyraz_1=i

    if warunek:
        jedna_lit+=1

    if len(zbior)==26:
        wszystkie_lac+=1

print(wszystkie_lac)
print(jedna_lit)
print(max_powt)
print(wyraz_1)
print()

#zad2
wystepowania_wzorcow={}
max_zad2=0
slowo_max2=''
for i in wzorce:
    wystepowania_wzorcow[i]=0

for i in teksty:
    for wzorzec in wzorce:
        wzorzec_we_slowie=0
        for indeks in range(len(i)):
            if i[indeks:len(wzorzec)]==wzorzec:
                wzorzec_we_slowie+=1
                wystepowania_wzorcow[wzorzec]+=1
        if wzorzec_we_slowie>max_zad2:
            max_zad2=wzorzec_we_slowie
            slowo_max2=i

    if wzorzec_we_slowie > max_zad2:
        max_zad2 = wzorzec_we_slowie
        slowo_max2 = i
max_wzorzec=[]
min_wzorce=[]
min_w=float('inf')
max_w=0
for slowo, wartosc in wystepowania_wzorcow.items():
    if min_w>wartosc:
        min_wzorce=[slowo]
        min_w=wartosc
    if min_w==wartosc:
        min_wzorce.append(slowo)
    if max_w<wartosc:
        max_w=wartosc
        max_wzorzec=slowo

finalne_min_wzorce=list(set(min_wzorce))



with open('wyniki7.txt','w')as wyniki:
    wyniki.write('7.1\n')
    wyniki.write(str(wszystkie_lac))
    wyniki.write('\n')
    wyniki.write(str(jedna_lit))
    wyniki.write('\n')
    wyniki.write(str(max_powt))
    wyniki.write('\n')
    wyniki.write(str(wyraz_1))
    wyniki.write('\n')
    wyniki.write('\n')
    wyniki.write('7.2\n')
    for i in finalne_min_wzorce:
        wyniki.write(i)
        wyniki.write('\n')
    wyniki.write('\n')
    wyniki.write(max_wzorzec)
    wyniki.write(f" {max_w}\n")
    wyniki.write('\n')
    wyniki.write(slowo_max2)









