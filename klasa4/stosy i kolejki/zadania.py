def sprawdz_nawiasy(tekst):
    stos=[]
    pary={')':'(',']':'[','}':'{'}
    for i in tekst:
        if i in pary.values(): #otwierajace
            stos.append(i)
        elif i in pary: #zamyakajce
            if not stos or stos[-1]!=pary[i]:
                return False
            stos.pop()
    return not stos

print(sprawdz_nawiasy("([])"))      # True
print(sprawdz_nawiasy("([)]"))      # False
print(sprawdz_nawiasy("((()))"))    # True
print(sprawdz_nawiasy("(()"))       # False
print(sprawdz_nawiasy("{[()]}"))    # True
print(sprawdz_nawiasy(""))

def odwroc_slowa(zdanie):
    lista=zdanie.split()
    return ' '.join(reversed(lista))

print(odwroc_slowa("Python jest super"))  # "super jest Python"
print(odwroc_slowa("Ala ma kota"))        # "kota ma Ala"