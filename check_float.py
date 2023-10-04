import re
def is_float(s):
    pattern=r'^[+-]?[0-9]*\.[0-9]+$'
    return bool(re.match(pattern,s))
T=int(input())
for i in range(T):
    string = input()
    if is_float(string):
        print("True")
    else:
        print("False")