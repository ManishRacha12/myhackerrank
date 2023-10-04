import array
a=input("enter string : ")
b=input("enter string to search for: ")
i=0
j=0
for k in a:
    for l in b:
        if a[i]==b[j]:
            print(i)
        i=i+1
