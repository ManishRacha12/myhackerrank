"""You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float.

"""

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    reversed_arr=numpy.flip(arr)
    return numpy.array(reversed_arr,float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
