#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # Write your code here
    arr=sorted(arr)
    for i in arr:
        s=len(arr)
        s1=(s+1)/2
        if s1==0:
            print(arr[s1])
            
        else:
            a=len(arr)/2
            b=a+1
            value=arr[a]+arr[b]
            print(value/2)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
