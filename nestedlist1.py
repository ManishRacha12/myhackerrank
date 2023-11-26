"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
"""

s=[]
for number in range(int(input())):
    name=input()
    score=float(input())
    s.append([name,score])
uni_sco=sorted(set(score for name,score in s))
sec_lowest=uni_sco[1]
result=sorted([name for name,score in s if score==sec_lowest])
for name1 in result:
    print(name1)