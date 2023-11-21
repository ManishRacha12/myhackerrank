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
X = int(input())
N = map(int,input().split())
x = int(input())
L = map(tuple,(map(int,input().split()) for _ in range(x)))
n = Counter(N)
p =0
for i in L:
    if i[0] in n.keys() and n[i[0]] >0 :
        n[i[0]] = n[i[0]]-1
        p = p+i[1]
print(p)