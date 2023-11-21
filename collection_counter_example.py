from collections import Counter
L=[1,2,3,4,2,3,4]
T=[(1,2),(2,3),(3,4)]
C=Counter(L)
for i in T:
    if i[0] in C.keys() and C[i[0]]>0:
        C[i[0]]=C[i[0]]-1
        print(f"processed {i[0]},remaining count : {C[i[0]]}")