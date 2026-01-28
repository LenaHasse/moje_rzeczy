
with open('liczby1.txt','r')as plik1:
    liczby1=[x.strip()for x in plik1]

    with open('liczby2.txt','r')as plik2:
        liczby2=[int(x) for x in plik2]

        #zad1
        maksymalna=''
        minimalna=''
        maksymalna_dec=0
        minimalna_dec=float('inf')

        for liczba in liczby1:
            dziesietna=int(liczba,8)
            if maksymalna_dec<dziesietna:
                maksymalna=liczba
                maksymalna_dec=dziesietna
            if minimalna_dec>dziesietna:
                minimalna=liczba
                minimalna_dec=dziesietna

        print(minimalna)
        print(maksymalna)

        #zad2
        dlugosc_ciagu=1
        najdluzszy_ciag=1
        pierwszy_wyraz_max=liczby2[0]
        pierwszy_wyraz=liczby2[0]
        poprzedni_wyraz=liczby2[0]
        for i in range(1,len(liczby2)):
            if liczby2[i]>=poprzedni_wyraz:
                dlugosc_ciagu+=1
                poprzedni_wyraz=liczby2[i]
            else:
                if dlugosc_ciagu>najdluzszy_ciag:
                    najdluzszy_ciag=dlugosc_ciagu
                    pierwszy_wyraz_max=pierwszy_wyraz
                dlugosc_ciagu=1
                poprzedni_wyraz=liczby2[i]
                pierwszy_wyraz=liczby2[i]

        print(najdluzszy_ciag)
        print(pierwszy_wyraz_max)

        #zad3
        TakaSamaWartosc=0
        wieksza1od2=0
        for i in range(len(liczby1)):
            dziesietna=int(liczby1[i],8)
            if dziesietna==liczby2[i]:
                TakaSamaWartosc+=1
            if dziesietna>liczby2[i]:
                wieksza1od2+=1

        print()

        print(TakaSamaWartosc)
        print(wieksza1od2)
        print()

        #zad4
        SzostkiWDziesietnym=0
        SzostkiWOsemkowym=0
        for i in range(len(liczby2)):
            wyraz=str(liczby2[i])
            for j in range(len(wyraz)):
                if wyraz[j]=='6':
                    SzostkiWDziesietnym+=1

        print(SzostkiWDziesietnym)

        for i in range(len(liczby2)):
            wyraz=oct(liczby2[i])[2:]
            for j in range(len(wyraz)):
                if wyraz[j]=='6':
                    SzostkiWOsemkowym+=1
        print(SzostkiWOsemkowym)




