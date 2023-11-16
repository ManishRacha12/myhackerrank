'''The first line contains integers  and  separated by a space.
The second line contains  integers, the elements of the array.
The third and fourth lines contain  integers,  and , respectively.
'''


input_line1=input()      #giving two input values separated by space
n,m=input_line1.split()     #splitting two values to both n and m variables
n=int(n)                    #converting n to int of n
m=int(m)                    #converting m to int of m

input_line2=input()         #taking multiple values on same line and storing them in array
values1=input_line2.split()     #splitting values into individual values
values1=[int(x) for x in values1 if len(values1)<=n]   #converting elements of array to int for only values less than len(n)

    
input_line3=input()             #taking multiple values on same line with separated space
A=input_line3.split()     #splitting values to individual values
A=[int(y) for y in A if len(A)<=m]   #converting values to int of each element in A till len(A)<=m

input_line4=input()             #taking multiple values with separated space
B=input_line4.split()         #splitting multiple values to both A and B variables
B=[int(z) for z in B if len(B)<=m]                      #convert to int in B till len(B)<=m
happiness=0
for i in values1:                   #for each element in array 
    if i in A:        #if each element in array belongs to A then increase happiness
        happiness=happiness+1
    elif i in B:                     #if each element in array belongs to B then decrease happiness
        happiness=happiness-1
print(happiness)
