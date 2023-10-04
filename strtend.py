import re
s=input("enter long string: ")                    
k=input("enter string to search: ")
pattern=rf'(?=({re.escape(k)}))'             #?= defines matches are not overlapping,  re.escape defines any special characters are treated as literal string                                            
m=re.finditer(pattern,s)                #finditer defines to find all non overlapping matches of the substring in string
k=re.search(pattern,s)              #search pattern string in string 
if k:
    for e in m:
        a=e.start(1),e.end(1)-1         #stores index values in a
        print(tuple(a))
else:
    o=-1,-1
    print(tuple(o))

