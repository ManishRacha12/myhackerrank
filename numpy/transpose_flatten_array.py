"""You are given a X integer array matrix with space separated elements ( = rows and  = columns).
Your task is to print the transpose and flatten results.

"""

import numpy
N,M=input().split()   #takes twp input values with space separated and convert each like below
N=int(N)            
M=int(M)
s=[]                    #create empty list
for i in range(N):
    arr=input().strip().split(' ')     #taking input
    arr=[int(x) for x in arr]
    s.append(arr)
arr=numpy.array(s)
print(numpy.transpose(arr))
print(arr.flatten())   

    