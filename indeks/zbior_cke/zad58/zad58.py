import math
with open ('dane_systemy1.txt', 'r') as plik1:
    lista_temp=[x.strip() for x in plik1]
    lista_S1=[(x.split()) for x in lista_temp]

    with open('dane_systemy2.txt', 'r') as plik2:
        lista_temp = [x.strip() for x in plik2]
        lista_S2 = [(x.split()) for x in lista_temp]

        with open('dane_systemy3.txt', 'r') as plik3:
            lista_temp = [x.strip() for x in plik3]
            lista_S3 = [(x.split()) for x in lista_temp]


            def dowolny_na_dziesietny(number,system):
                ujemna=number.startswith('-')
                if ujemna:
                    number=number[1:]

                wynik=0
                potega=1
                for cyfra in reversed(number):
                    wynik+=int(cyfra)*potega
                    potega*=system
                if ujemna:
                    wynik=-wynik
                return wynik


            #zad1

            #s1
            najnizsza_s1=float('inf')
            for i in lista_S1:
                temperatura=dowolny_na_dziesietny( i[1],2)
                if temperatura<najnizsza_s1:
                    najnizsza_s1=temperatura

            najnizsza_s1=bin(najnizsza_s1)



            # s2
            najnizsza_s2 = float('inf')
            for i in lista_S2:
                temperatura = dowolny_na_dziesietny(i[1], 4)
                if temperatura < najnizsza_s2:
                    najnizsza_s2 = temperatura
            najnizsza_s2=bin(najnizsza_s2)
            # s3
            najnizsza_s3 = float('inf')
            for i in lista_S3:
                temperatura = dowolny_na_dziesietny(i[1], 8)
                if temperatura < najnizsza_s3:
                    najnizsza_s3 = temperatura
            najnizsza_s3=bin(najnizsza_s3)


            # konwersja na ladny binarny

            if str(najnizsza_s1)[0]=='-':
                najnizsza_s1=f'-{str(najnizsza_s1)[3:]}'
            else:
                najnizsza_s1=str(najnizsza_s1)[2:]


            if str(najnizsza_s2)[0]=='-':
                najnizsza_s2=f'-{str(najnizsza_s2)[3:]}'
            else:
                najnizsza_s2=str(najnizsza_s2)[2:]


            if str(najnizsza_s3)[0]=='-':
                najnizsza_s3=f'-{str(najnizsza_s3)[3:]}'
            else:
                najnizsza_s3=str(najnizsza_s3)[2:]

            print(najnizsza_s1)
            print(najnizsza_s2)
            print(najnizsza_s3)
            print()


            #zad2
            ilosc_zad2=0
            for i in range(1095):
                oczekiwany_stan=12+i*24
                czas_S1=dowolny_na_dziesietny(lista_S1[i][0],2)
                czas_S2 = dowolny_na_dziesietny(lista_S2[i][0], 4)
                czas_S3 = dowolny_na_dziesietny(lista_S3[i][0], 8)
                if czas_S1!=oczekiwany_stan and czas_S2!=oczekiwany_stan and czas_S3!=oczekiwany_stan:
                    ilosc_zad2+=1

            print(ilosc_zad2)
            print()
            #zad3
            ile_zad3=0
            rekord_s1=float('-inf')
            rekord_s2=float('-inf')
            rekord_s3=float('-inf')
            for i in range(1095):
                temperatura_S1=dowolny_na_dziesietny(lista_S1[i][1],2)
                temperatura_S2 = dowolny_na_dziesietny(lista_S2[i][1], 4)
                temperatura_S3 = dowolny_na_dziesietny(lista_S3[i][1], 8)
                rekord=False

                if temperatura_S1>rekord_s1:
                    rekord_s1=temperatura_S1
                    rekord=True

                if temperatura_S2>rekord_s2:
                    rekord_s2=temperatura_S2
                    rekord = True

                if temperatura_S3>rekord_s3:
                    rekord_s3=temperatura_S3
                    rekord = True

                if rekord:
                    ile_zad3+=1


            print(ile_zad3)
            print()

            #zad4
            najwyzszy_skok=float('-inf')
            for i in range(1095):
                for j in range(1095):
                    if i!=j:
                        temperatura_i = dowolny_na_dziesietny(lista_S1[i][1], 2)
                        temperatura_j = dowolny_na_dziesietny(lista_S1[j][1], 2)
                        r=(temperatura_i-temperatura_j)**2
                        modul=abs(i-j)

                        skok_temperatur=math.ceil(r/modul)

                        if najwyzszy_skok<skok_temperatur:
                            najwyzszy_skok=skok_temperatur

            print(najwyzszy_skok)






