n=int(input())
arr=list(map(int,input().split()))
arr=sorted(arr)
list1=[]
for i in arr:
    if arr.count(i)>1:
        list1.append(arr.count(i)-1)
    
print(list1)