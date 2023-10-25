n=int(input())
alph='abcdefghijklmnopqrstuvwxyz'      #give lowercase alphabets as a string
for i in range(n-1,0,-1):               #loop runs in reverse order 
    row='-'.join(alph[n-1:i:-1]+alph[i:n])   #concatination with - in between two arrays where one array gives alphabets from n-1 to i where i points to last alphabet
#                                               alph[i:n] here it gives values between i and n where n is n-1 then concatination
    print(row.center(4*n-3,'-'))               #making the whole row into center and adding - in between spaces
for j in range(n):                                  #we reverse the loop, starting from 0 and increasing to size. 
    row1='-'.join(alph[n-1:j:-1]+alph[j:n])         #same like above
    print(row1.center(4*n-3,'-'))           