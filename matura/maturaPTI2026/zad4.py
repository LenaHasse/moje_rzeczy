with open('tekst_przyklad.txt', 'r')as plik:
    lista=[]
    for linia in plik:
        for slowo in linia.strip().split():
            lista.append(slowo)
    print(lista)

    #ZAD1
    najdluzszy_podciag=1
    podciag=1
    wyrazy_najdluzszego_podciagu=lista[0]
    wyrazy_podciagu=lista[0]

    for i in range(0,len(lista)-1):
            if len(lista[i])<len(lista[i+1]):
                wyrazy_podciagu+=' '+lista[i+1]
                podciag+=1

                if podciag>najdluzszy_podciag:
                    najdluzszy_podciag=podciag
                    wyrazy_najdluzszego_podciagu=wyrazy_podciagu
            else:
                podciag=1
                wyrazy_podciagu=lista[i+1]
    print(najdluzszy_podciag)
    print(wyrazy_najdluzszego_podciagu)

    #zad2
    nastepniki={}
    for i in range(len(lista)-1):
        obecne_slowo=lista[i]
        nastepne_slowo=lista[i+1]

        if obecne_slowo not in nastepniki:
            nastepniki[obecne_slowo]={}

        nastepniki[obecne_slowo][nastepne_slowo] = nastepniki[obecne_slowo].get(nastepne_slowo, 0) + 1

    zdanie=['the']
    biezace_slowo='the'
    while True:
        if biezace_slowo not in nastepniki:
            break
        mozliwe_nastepniki=nastepniki[biezace_slowo]

        max_czestosc=0
        najlepsi=[]
        for slowo, czestosc in mozliwe_nastepniki.items():
            if czestosc>max_czestosc:
                max_czestosc=czestosc
                najlepsi=[slowo]
            elif czestosc==max_czestosc:
                najlepsi.append(slowo)

        najlepszy_nastepnik=sorted(najlepsi)[0]

        if najlepszy_nastepnik in zdanie:
            break

        zdanie.append(najlepszy_nastepnik)
        biezace_slowo=najlepszy_nastepnik
print(' '.join(zdanie))



