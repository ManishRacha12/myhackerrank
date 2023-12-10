from itertools import product
A=map(int,input().split())
B=map(int,input().split())
A=set(A)
B=set(B)
AB=(list(product(A,B)))
for x in AB:
    print(x,end=" ")