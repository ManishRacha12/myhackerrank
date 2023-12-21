
def lonelyinteger(a):
    for i in a:
        if a.count(i)<2:
            print(i)
            
            
    
        
    



if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = lonelyinteger(a)

