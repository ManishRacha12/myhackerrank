'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
hello

'''
if __name__ == '__main__':
    N = int(input())
    my_list = []

    for _ in range(N):
        command = input().split()

        if command[0] == 'insert':
            my_list.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(my_list)
        elif command[0] == 'remove':
            my_list.remove(int(command[1]))
        elif command[0] == 'append':
            my_list.append(int(command[1]))
        elif command[0] == 'sort':
            my_list.sort()
        elif command[0] == 'pop':
            my_list.pop()
        elif command[0] == 'reverse':
            my_list.reverse()
