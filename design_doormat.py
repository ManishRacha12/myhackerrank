"""Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters."""
def print_door_mat(rows, columns):
    for i in range(1, rows, 2):
        pattern = (".|." * i).center(columns, '-')
        print(pattern)

    welcome_line = 'WELCOME'.center(columns, '-')
    print(welcome_line)

    for i in range(rows - 2, 0, -2):
        pattern = (".|." * i).center(columns, '-')
        print(pattern)

# Example usage with mat size 7 (you can change this value)
mat_size = int(input())
mat_width = mat_size * 3
print_door_mat(mat_size, mat_width)
