import math
# stała złożoność obliczeniowa, niezaleznie od wartosci argumentu ma ta sama wartosc

def wzor_herona(a,b,c):
    p=(a+b+c)/2
    area_triangle=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return area_triangle


print(f'{wzor_herona(6,7,8):.2f}') # ciekawe formatowanie

#złożoność logarytmiczna, bo za kazdym razem dzieli zakres na pol, liczba krokow
# rosnie bardzo wolno wraz ze wzrostem liczby elementow
def binary_search(sorted_array,target):
    left,right=0, len(sorted_array)-1

    while left <=right:
        mid=(left+right)//2

        if sorted_array[mid]==target:
            return mid
        elif sorted_array[mid]<target:
            left=mid+1
        else:
            right=mid-1

    return -1

sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
result = binary_search(sorted_array, target)
if result != -1:
    print(f"Element {target} znaleziony na indeksie {result}")
else:
    print(f"Element {target} nie został znaleziony")

#zlozonosc liniowa bo wykonuje tyle operacji ile jest argumentow podanych
def thehighestnumber(numbers):
    n=len(numbers)

    max_number=numbers[0]
    for i in range(n):
        if max_number<numbers[i]:
            max_number=numbers[i]

    return max_number

numbers = [1, 4, 7, 3, 9, 10, 2, 8, 4]
print(thehighestnumber(numbers))

#zlozonosc liniowo-logarytmiczna, bo dzieli liste na pol, tak jak w binary search, i w rekurencji bada kazdy element
def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid=len(arr)//2
    left_half=arr[:mid]
    right_half=arr[mid:]

    left_half=merge_sort(left_half)
    right_half=merge_sort(right_half)

    return merge(left_half,right_half)

def merge(left,right):
    result=[]
    i=j=0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])

    return result


arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = merge_sort(arr)
#print("Niesortowana lista:", arr)
#print("Posortowana lista:", sorted_arr)

#zlozonosc kwadratowa bo uzywa dwoch zagniezdzonych petli for i kazda wykonuje ja n-1 razy
def tabliczka_mnozenia(n):
    for i in range(1,n):
        for j in range(1,n):
            print(f"{i*j}",end='\t')
        print()
#tabliczka_mnozenia(11)

#zlozonosc szescienna, bo sa 3 petle wykonuje operacje n -1 razy
def poor_trojkipitagorjskie(n):
    for a in range(1,n):
        for b in range(1,n):
            for c in range(1,n):
                if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
                    print(f'{a},{b},{c}')

#poor_trojkipitagorjskie(100)

#zlozonosc wykladnicza, bo kazdy wyraz oblicza dwa poprzednie
def fibonacci(n:int)->int:
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

#print(fibonacci(10))

#zlozonosc O(n!) liczba operacji rosniwe wraz z rozmiarem danych wejsciowych
def generate_permutations(arr,start,end):
    if start==end:
        print(' '.join(map(str,arr)))
    else:
        for i in range(start,end+1):
            arr[start],arr[i]=arr[i],arr[start]
            generate_permutations(arr,start+1,end)
            arr[start],arr[i]=arr[i],arr[start]

n = 5
arr = list(range(1, n + 1))
print("Permutacje zbioru:")
generate_permutations(arr, 0, n - 1)