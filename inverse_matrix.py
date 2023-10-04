n1=input("enter no of values in array1: ")
a1=list(map(int,input("enter values: ")))   #takes values to array matrix
print(a1)
c1=int(a1[0]*a1[3])-(a1[1]*a1[2])    #performs ad-bc 
c2=1/c1
c=a1[0]
a1[0]=a1[3]
a1[1]=-a1[1]
a1[2]=-a1[2]
a1[3]=c
print(c2,'*',a1)    #prints inverse matrix
