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
values1=[int(x) for x in values1]       #converting each element in values1 to int

input_line3=input()             #taking multiple values on same line with separated space
values2=input_line3.split()     #splitting values to individual values
values2=[int(y) for y in values2]   #converting values to int of each element in values2

input_line4=input()             #taking multiple values with separated space
A,B=input_line4.split()         #splitting multiple values to both A and B variables
A=int(A)                        #convert to int
B=int(B)                        #convert to int

n1=set(values1)         #converting values1 to set from list
m1=set(values2)            #converting values2 to set from list
happiness=0

for i in n1:
    if i == A:
        happiness=happiness+1
    elif i == B:
        happiness=happiness-1
print(happiness)