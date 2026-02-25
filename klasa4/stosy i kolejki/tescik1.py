#bubble sort
def bubble_sort(tab):
    n=len(tab)
    for i in range(n-1):
        for j in range(n-1-i):
            if tab[j]>tab[j+1]:
                tab[j],tab[j+1]=tab[j+1],tab[j]
    return tab

#insertion sort
def insertion_sort(tab):
    n=len(tab)
    for i in range(1,n):
        klucz=tab[i]
        j=i-1

        while j>=0 and tab[j]>klucz:
            tab[j+1]=tab[j]
            j-=1

        tab[j+1]=klucz

    return tab


print(insertion_sort([5,6,2,5,8]))

#merge sort
def scal(lewa,prawa):
    wynik=[]
    i=j=0

    while i<len(lewa) and j<len(prawa):
        if lewa[i] <= prawa[j]:
            wynik.append(lewa[i])
            i+=1
        else:
            wynik.append(prawa[j])
            j+=1

    wynik.extend(lewa[i:])
    wynik.extend(prawa[j:])
    return wynik

def sortowanie_przez_scalanie(tab):
    if len(tab)<=1:
        return tab

    srodek=len(tab)//2
    lewa=sortowanie_przez_scalanie(tab[:srodek])
    prawa=sortowanie_przez_scalanie(tab[srodek:])

    return scal(lewa,prawa)

#quick sort
def quicksort(tab):
    if len(tab)<=1:
        return tab

    pivot=tab[len(tab)//2]

    mniejsze=[x for x in tab if x<pivot]
    rowne=[x for x in tab if x==pivot]
    wieksze=[x for x in tab if x > pivot]
    return quicksort(mniejsze)+rowne+quicksort(wieksze)
