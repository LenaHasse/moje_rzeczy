import math
from math import gcd

def pole_trojkata(a:int,h:int):
    area=0.5*a*h
    return area


def pole_trojkata_rownobocznego(a:float):
    area=a**2*math.sqrt(3)/4
    return area

def warunek_trojkata(a:int,b:int,c:int):
    if a+b>c and a+c>b and b+c>a:
        return 'z tych bokow mozna zbudowac trojkat'
    else:
        return 'z tych bokow nie mozna zbudowac trojkata'

def sprawdzanie_pitagorasa(a:int,b:int,c:int):
    if a+b>c and b+c>a and c+a>b:
        if a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+a**2==b**2:
            return 'z tych bokow mozna zbudowac trojkat prostokatnych'
        else:
            return 'z tych bokow nie mozna zbudowac trojkata prostokatnego, ale inny juz mozna'
    else:
        return 'z tych bokow nie mozna zbudowac trojkata'

#wzor herona w pliku zlozonosc obliczeniowa

def pole_trojkata_z_wierzcholkow(A,B,C):
    xA,yA=A
    xB,yB=B
    xC,yC=C

    pole=abs(xA*(yB-yC)+xB(yC-yA)+xC(yA-yB))/2
    return pole

def pick_triangle_area(A,B,C,I):

    #liczba pk w bokach
    B_AB=gcd(abs(B[0]-A[0]), abs(B[1]-A[1]))+1
    B_BC=gcd(abs(C[0]-B[0]),abs(C[1]-B[1]))+1
    B_CA=gcd(abs(A[0]-C[0]), abs(A[1]-C[1]))+1

    B_total=B_CA+B_BC+B_AB-3

    P=I+B_total/2-1
    return P

# A = (0, 0)
# B = (4, 0)
# C = (0, 3)
# I = 3
#
# pole = pick_triangle_area(A, B, C, I)
# print("Pole trójkąta kratowego:", pole)

def pole_trojkata_sin(ab,ac,kat_A_stopnie):
    kat_A_radiany=math.radians(kat_A_stopnie)
    pole=0.5*ab*ac*math.sin(kat_A_radiany)
    return pole




