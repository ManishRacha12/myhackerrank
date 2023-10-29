
#converts elements in list to string using join
l=['a','b','c','d']
re=''.join(l)
print(re)



#To check leap or not without using % operator
leap=int(input("enter year"))
if (leap//4)*4==leap or (leap//100)*100==leap//100:
    print("leap year")
else:
    print("non leap")