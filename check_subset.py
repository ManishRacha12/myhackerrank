''''
You are given two sets,  and .
Your job is to find whether set  is a subset of set .

If set  is subset of set , print True.
If set  is not a subset of set , print False.

Input Format

The first line will contain the number of test cases, .
The first line of each test case contains the number of elements in set .
The second line of each test case contains the space separated elements of set .
The third line of each test case contains the number of elements in set .
The fourth line of each test case contains the space separated elements of set .

'''''
T=int(input())
if T>0 and T<21:
    for i in range(T):
        A=int(input())
        if A>0 and A<1001:
            A=input().split()
            B=int(input())
            if B>0 and B<1001:
                B=input().split()
                A=set(A)
                B=set(B)
                if A.issubset(B):
                    print("True")
                else:
                    print("False")
            else:
                print("False")
        else:
            print("False")
else:
    print("False")