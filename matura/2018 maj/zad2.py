X=[-3,2,5,7,2,-8]
Y=[5,8,2,7,9,3]
dzielenie=[]
for i in range(len(X)):
    dzielenie.append(X[i]/Y[i])
print(dzielenie)
def najblizszy_szczyt(X,Y):
    najmniejsza=[X[0],Y[0]]
    for i in range(1,len(X)):
        if najmniejsza[0]/najmniejsza[1]>X[i]/Y[i]:
            najmniejsza=[X[i],Y[i]]
    return najmniejsza

wynik=[]


