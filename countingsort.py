def count_occurrences(arr):
    # Initialize an empty dictionary to store the counts
    count_dict = {}

    # Count the occurrences of each value in the input array
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1

    # Convert the dictionary to a list of tuples (value, count)
    result = [(key, value) for key, value in count_dict.items()]

    return result

# Example input
input_numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5, 5]

# Count occurrences
occurrences = count_occurrences(input_numbers)

# Print the result
for value, count in occurrences:
    print(f"{value}: {count} times")
