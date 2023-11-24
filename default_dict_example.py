from collections import defaultdict
'''
d=defaultdict(list)      
d['first_name'].append("Manish")
d['last_name'].append("Racha")
d['first_name'].append("Sai Teja")
d['last_name'].append("Vempati")
for i in d.items():
    print(i)
    
'''
list1=['apple','banana','mango','apple','grapes','banana','apple']
counter=defaultdict(int)
for each_item in list1:
    counter[each_item]=counter[each_item]+1
print(counter)