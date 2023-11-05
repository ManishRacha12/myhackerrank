py = [['Harry', 37.21], ['Berry', 37.21], ['cina', 37.2], ['Akriti', 41], ['Harsh', 39]]
ab=sorted(py,key=lambda x:x[1])
list1=[stu for stu in ab for j in stu if j==ab[1]]
print(list1)