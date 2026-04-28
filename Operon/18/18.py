with open('trzyliczby.txt','r')as plik:
    lista_temp=[x.strip()for x in plik]
    trzyliczby=[]
    for i in lista_temp:
        a,b,c=i.split()
        trzyliczby.append([a,b,c])
print(trzyliczby)

#zad1
def wykryj_system(liczba):
    lista=[]
    for i in liczba:
        if i.isdigit():
            lista.append(int(i))
        else:
            lista.append(ord(i)-ord('A')+10)
    najwieksza=max(lista)
    return max(2,najwieksza+1)

print(wykryj_system('4BA9'))

for i in trzyliczby:
    