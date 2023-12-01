def palindrome(string1):
    s1=string1.lower()
    return s1==s1[::-1]

str1=input()
res=palindrome(str1)
if res:
    print("palindrome")
else:
    print("not palindrome")