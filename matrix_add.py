import array
n=int(input("enter no of values in array:"))
n1=int(input("enter no of values in array:"))
a1=list(map(int,input("enter array values:")))
a2=list(map(int,input("enter array values:")))
print(a1)
print(a2)
k=0
l=0
if n==n1:
    for i in a1:
        for j in a2:
            c=a1[k]+a2[l]
        print(c)
        k=k+1
        l=l+1
else:
    print("array is invalid")