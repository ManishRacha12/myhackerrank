'''The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.
For the first word in group B, 'a', it appears at positions  and  in group A. The second word, 'c', does not appear in group A, so print .

'''

from collections import defaultdict
d=defaultdict(list)             #creates a defaultdict with empty list as factory function as an argument
N=list(map(int,input().split()))    #mapping two integers to N in a list of N

for i in range(N[0]):           #for each iteration in range of N[0] 
    d[input()].append(i+1)      #taking input as a key and appending with increment as index as value each time

for j in range(N[1]):           #for each iteration in range of N[1]
    k=input()                   #user input to k
    if len(d[k])!=0:            #It then checks if the list associated with the input string in the defaultdict (d[k]) is not empty
        print(*d[k])            #then it unpack the list and prints the value which is a index 
    else:
        print(-1)               
        


