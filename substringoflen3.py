s=input()
res=[s[i:i+3] for i in range(0,len(s),1)]
for i in res:
    if(len(i)==3):
        print(i)
