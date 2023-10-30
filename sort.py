#sort strings in list
list1=['1','4','0','33','2','4','5','6']
final_list=[int(i) for i in list1]   #convert string to int 
final_list.sort()       #sort int elements
print(final_list)