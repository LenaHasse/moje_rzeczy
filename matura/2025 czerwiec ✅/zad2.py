with open('liczby1.txt','r')as plik:
    liczby=[int(x)for x in plik]

def ciecia(k):
    d=0
    temp=k
    while temp>0:
        temp//=10
        d+=1

    polowa=d//2
    b=k%10**polowa
    k//=10**polowa
    a=k
    return a,b
#zad2
def nwd(a,b):
    x=0
    while b!=0:
        x=a%b
        a,b=b,x
    return a

zad2=[]

for i in liczby:
    a,b=ciecia(i)
    if nwd(a,b)==1:
        zad2.append(i)

print(len(zad2))
print()
