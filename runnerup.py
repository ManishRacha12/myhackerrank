if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list1=list(arr)
    max1=max(list1)
    result=[x for x in list1 if x<max1]
    max2=max(result)
    print(max2)