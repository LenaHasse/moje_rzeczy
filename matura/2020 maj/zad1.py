i=0
A=[56,7,2,98,52,45,83,3]
n=len(A)
while i<n-1:
    if A[i]>A[i+1]:
        pom=A[i]
        A[i]=A[i+1]
        A[i+1]=pom
    i+=2
i=0
x=A[i]
y=A[i+1]
while i<n-3:
    if A[i+2]<x: x=A[i+2]
    if A[i+3]>y: y=A[i+3]
    i+=2

print(x)
print(y)
print(A)