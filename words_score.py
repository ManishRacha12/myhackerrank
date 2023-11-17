'''The input is read by the provided locked code template. In the first line, there is a single integer  denoting the number of words. In the second line, there are  space-separated lowercase words.

'''
n=int(input())
words=input()
string_words=words.split()
string_words=[x for x in string_words if len(string_words)<=n]
vowels=['a','e','i','o','u','y']
score=0
count=0
for word in string_words:
    for char in word:
        if char in vowels:
            count=count+1
    if count%2==0:
        score=score+2
        print("even score",score)
    else:
        score=score+1
        print("odd score",score)
    count=0
print(score)
    