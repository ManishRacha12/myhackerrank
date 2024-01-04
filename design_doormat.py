"""Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters."""
def doormat(rows,columns):
    for i in range(1,rows,2):
        pattern=(".|."*i).center(columns,'-')   #using center method padding to center based on columns with '-' and using pattern '.|.'
        print(pattern)
    welcome_line='WELCOME'.center(columns,'-')
    print(welcome_line)
    for i in range(rows-2,0,-2):
        pattern=(".|."*i).center(columns,'-')
        print(pattern)


N,M=map(int,input().split())
doormat(N,M)