import re

pattern = r'[^aeiouAEIOU\s]*([\+\-aeiouAEIOU]{2,})[^aeiouAEIOU\s]'
string=input()
match1=re.findall(pattern,string)
if match1:
    for i in match1:
        print(i)
else:
    print(-1)