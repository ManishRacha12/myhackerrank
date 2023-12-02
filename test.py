'''
Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of  country stamps.

Find the total number of distinct country stamps.

Input Format

The first line contains an integer , the total number of country stamps.
The next  lines contains the name of the country where the stamp is from.

'''
N=int(input())              #takes N number of countries
input_line=[]               #creates an empty list
for i in range(N):          #for each in range(N) 
    i=input()               #assigns input each time to i
    input_line.append(i)            #adding each element to empty list
result=set(input_line)          #converting list to set to remove duplicates
print(len(result))          #print len of entries after removing duplicates
    