x = 1
y = 1
z = 2

list=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k ==3:
                continue
            list.append((i,j,k))
print(list)

"""

sai =[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=3]
print(sai)

"""