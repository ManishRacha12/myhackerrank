"""
Let's create a scenario called the "Substring Game":

Problem Statement:

Two players, Alice and Bob, are given the same string.
Both players have to make substrings using the letters of the string.
Alice has to make substrings of even length.
Bob has to make substrings of odd length.
The game ends when both players have made all possible substrings according to their respective lengths.
Scoring:

A player gets +1 point for each occurrence of the substring in the string.
"""

def game(string):
    s=string
    l=len(s)
    Alice_score, Bob_score = 0,0
    for i in range(l):
        for j in range(i+2,l+1,2):
            substring=s[i:j]
            if len(substring)%2==0:
                Alice_score=Alice_score+1
            else:
                Bob_score+=1
    print(Alice_score,Bob_score)
    """if Alice_score>Bob_score:
        print(f"Alice_score {Alice_score}")
    elif Bob_score>Alice_score:
        print(f"Bob_Score {Bob_score}")
    else:
        print("Draw")"""
        
if __name__=='__main__':
    b=input()
    game(b)