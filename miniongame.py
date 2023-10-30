def minion_game(string):
    l=len(string)               #takes the length of input string
    kevin_score,Stuart_score=0,0    #initially assign both scores to 0
    vowel='AEIOUaeiou'                  #assign vowels to variable vowel
    for i in range(l):
        if string[i] in vowel:                  #check condition if string of i has a vowel character
            kevin_score=kevin_score+l-i             #if yes then increase score by adding kevin_score plus total length - current iteration value
        else:
            print(i)
            Stuart_score=Stuart_score+l-i
    if kevin_score>Stuart_score:
        print(f"kevin {kevin_score}")
    elif Stuart_score>kevin_score:
        print(f"Stuart {Stuart_score}")
    else:
        print("DRAW")
    print(l)       
    # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)