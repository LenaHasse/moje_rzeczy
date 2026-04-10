with open('odbiorcy.txt', 'r')as plik:
    odbiorcy=[int(x.strip()) for x in plik]

#zad2
zad2=0
for i in range(1,1024):
    if i not in odbiorcy:
        zad2+=1

print(zad2)

#zad3
pakiety=[]
for i in range(len(odbiorcy)):
    pakiety.append(i+1)
print(pakiety)
warunek=True
zad3=None

nr_rundy=0
def runda(lista):
    pakiet=list(lista)
    for i in range(len(lista)):
        lista[i]=pakiet[odbiorcy[i]-1]
    return lista

while warunek:
    temp = runda(pakiety)
    nr_rundy += 1
    for i in range(len(temp)):
        if temp[i] == i + 1:
            zad3 = (nr_rundy, i + 1)
            warunek = False
            break

print(zad3)