list=[1,2,3,4]
result=[x**2 for x in list]   # this give the power of 2 for each element in array
print(result)

list1=[3,4,5,6]
result2=[y**2 for y in list1 if y%2==0]
print(result2)

a=iter(list)   #here a is an object we created to call builtin iter function with list
print(next(a))   #we retrive the element in the list one at a time using next 