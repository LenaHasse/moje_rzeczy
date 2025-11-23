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


            #zad2
            poczatek=12
            for i in range(1095):
                dowolny_na_dziesietny(S1[i][])



