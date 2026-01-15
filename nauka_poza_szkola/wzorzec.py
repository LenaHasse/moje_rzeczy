def wzorzec(tekst,wzorzec):
    len_tekst=len(tekst)
    len_wzorzec=len(wzorzec)
    pozycje=[]
    for i in range(len_tekst-len_wzorzec):
        dopasowano=True
        for j in range(len_wzorzec):
            if tekst[i+j]!=wzorzec[j]:
                dopasowano=False
        if dopasowano:
            pozycje.append(i)
    return pozycje




tekst='Kot ma Ale a Ala ma kota'
wzorzec1='ma'
print(wzorzec(tekst,wzorzec1))