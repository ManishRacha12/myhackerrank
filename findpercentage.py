n=int(input())
s={}
for i in range(n):
    name,*line=input().split()      #input split will take input from user and assign to name and line(marks values) till the loop runs
    scores=list(map(float,line))   #scores -> each value in line will be converted to float using map and then converted to list of float values
    s[name]=scores    #scores will get assign to each name in each iteration
print(s)   #prints whole dictionary with scores and names 
query_name=input()      #asking user to check scores of student name
sum=0
counter=0
if query_name in s:    #checking name is present in dict
    for i in s[query_name]:      #running iteration over values in query_name key inside dict 
        sum=sum+i                 #adding each number   
        counter=counter+1         
    Avg=sum/counter
    formattedavg="{:.2f}".format(Avg)    #converts Avg to 2 decimal float value using this ""{:.2f}".format(variablename)"
    print(formattedavg)