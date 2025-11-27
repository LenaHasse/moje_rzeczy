def choinka(x):
    poczatkowe=x
    for i in range(1,(2*x)+1,2):
        print(x*' ',i*'*')
        x-=1
    print(poczatkowe*' ','|')

choinka(4)