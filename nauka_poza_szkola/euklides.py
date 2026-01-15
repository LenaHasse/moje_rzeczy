def euklides1(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def euklides2(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

def euklides3(a,b):
    if b==0:
        return a
    else:
        return euklides3(b,a%b)


print(euklides1(1989, 867))
print(euklides2(1989, 867))
print(euklides3(1989, 867))