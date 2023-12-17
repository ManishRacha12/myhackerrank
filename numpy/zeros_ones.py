import numpy

N1,N2,N3=input().strip().split(' ')
N1=int(N1)
N2=int(N2)
N3=int(N3)
print(numpy.zeros((N1,N2,N3),dtype=numpy.int))
print(numpy.ones((N1,N2,N3),dtype=numpy.int))