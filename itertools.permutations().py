from itertools import permutations
s,k=input().split()
k=int(k)
s=sorted(list(permutations(s,k)))
for x in s:
    res="".join(x)
    print(res)