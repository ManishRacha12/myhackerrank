import re
pattern2 = r'[*+-.,]+'
Input1=input()
result=re.split(pattern2,Input1)
print('\n'.join(result))