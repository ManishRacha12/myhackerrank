'''
is a shoe shop owner. His shop has  number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money  earned.

Input Format

The first line contains , the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.

Constraints
'''

from collections import Counter
X=int(input())      #No of shoes
X_list=map(int,input().split())     #The second line contains the space separated list of all the shoe sizes in the shop.
N=int(input())          #The third line contains N, the number of customers.
N_xi=map(tuple,(map(int,input().split()) for _ in range(N)))    #The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.
shoe_list=Counter(X_list)
sum=0
for each_item in N_xi:
    if each_item[0] in shoe_list.keys() and shoe_list[each_item[0]]>0:
        shoe_list[each_item[0]]=shoe_list[each_item[0]]-1
        sum=sum+each_item[1]
print(sum)
        

