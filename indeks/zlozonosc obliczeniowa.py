import math

def wzor_herona(a,b,c):
    p=(a+b+c)/2
    area_triangle=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return area_triangle


print(f'{wzor_herona(6,7,8):.2f}') # ciekawe formatowanie