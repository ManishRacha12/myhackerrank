"""You are given a space separated list of nine integers. Your task is to convert this list into a X NumPy array.

"""


import numpy
N=input().split(' ')
s=[]
for i in N:
    s.append(int(i))
print(numpy.reshape(s,(3,3)))
