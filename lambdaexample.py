'''Consider a list of integers, and use the filter() function along with a lambda function to create a new list that contains only the even numbers from the original list.
'''

list1=[1,2,3,3,4,5,6,7,8,9,10]
filter_numbers=list(filter(lambda a : a%2==0,list1))
print(filter_numbers)


'''Suppose you have a list of names in the format "First Last" (e.g., "John Doe"). Write a Python expression using map() and lambda to create a new list of initials for each name.

'''
original_names = ["John Doe", "Alice Smith", "Bob Johnson", "Eve Adams"]
initials=[]
for i in original_names:
    a="".join(map(lambda x:x[0].upper(),i.split()))
    initials.append(a)
print(initials)