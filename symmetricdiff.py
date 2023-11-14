'''
Task
Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.


'''

M=int(input())
m1=set(map(int, input().split()))
N=int(input())
n1=set(map(int, input().split()))
a=sorted(set(m1-n1))
b=sorted(set(n1-m1))
c=a+b
d=sorted(c)
for i in d:
    print(i)


