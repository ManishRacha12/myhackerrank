"""ou are given two integer arrays of size X and X ( &  are rows, and  is the column). Your task is to concatenate the arrays along axis .

Input Format

The first line contains space separated integers ,  and .
The next  lines contains the space separated elements of the  columns.
After that, the next  lines contains the space separated elements of the  columns."""

import numpy
N,M,P=input().strip().split(' ')
N,M,P=int(N),int(M),int(P)
x1=[]
y1=[]

for i in range(N):
    x=input().split()
    x=[int(y) for y in x]
    x1.append(x)
for j in range(M):
    y=input().split()
    y=[int(x) for x in y]
    y1.append(y)

arr1=numpy.array(x1)
arr2=numpy.array(y1)
print(numpy.concatenate((arr1,arr2),axis=0))