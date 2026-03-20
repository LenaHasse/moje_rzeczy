def bubbleSort(tab):
    n=len(tab)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if tab[j]>tab[j+1]:
                tab[j],tab[j+1]=tab[j+1],tab[j]
    return tab

print(bubbleSort([5, 3, 8, 1, 2]))