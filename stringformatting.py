def print_formatted(number):
    numbers=[]
    width=len(bin(number)[2:])
    # your code goes here
    for i in range(1,number+1):
        deci=str(i)
        octa=oct(i)[2:]
        hexa=hex(i)[2:].upper()
        bi=bin(i)[2:]
        res=f"{deci:>{width}} {octa:>{width}} {hexa:>{width}} {bi:>{width}}"
        numbers.append(res)
    for i in numbers:
        print(i)
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)