import re
input1=input()
input2=re.sub(r'[^a-zA-Z0-9]',' ',input1)  #removing or subtracting extra characters that are not alphanumeric
match_var = re.search(r'(\w)\1',input2)  #searching for group words(\w) followed by numbers from input2 which was already filtered
if match_var:
    print(match_var.group(1))
else:
    print(-1)