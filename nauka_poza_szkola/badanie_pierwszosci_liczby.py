def czypierwsza_naiwna(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True


print(czypierwsza_naiwna(3))

def czypierwsza(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False

    for i in range(3,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print()

print(czypierwsza(59))