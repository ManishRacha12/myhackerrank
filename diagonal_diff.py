n=int(input())
arr=[]
for i in range(n):
    i1=list(map(int,input().split()))
    arr.append(i1)
print(arr)
rows=len(arr)
cols=len(arr[0])
frt_diagonal=sum(arr[i][i] for i in range(min(rows,cols)))
sec_diagonal=sum(arr[i][cols-i-1] for i in range(min(rows,cols)))
print(abs(frt_diagonal-sec_diagonal))