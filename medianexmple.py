arr=[0,1,2,3,4,5,6]
s=len(arr)
s1=int((s+1)/2)
if s1%2==0:
    print(arr[s1-1])
else:
    s2=int(len(arr)/2)
    s3=int(len(arr)/2)+1
    sum=arr[s2-1]+arr[s3-1]
    print(sum/2)
    
    
