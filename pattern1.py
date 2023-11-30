N=int(input())
M=N*3
for i in range(N):
    for j in range(N-i+2,0,-1):
        print("-",end="")
    print(".",end="")
    print("|",end="")
    print(".")       