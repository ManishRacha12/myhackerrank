import re

def capitalize_names_with_spaces(input_str):
    # Split the input string into words using regular expressions to preserve spaces
    words = re.split(r'(\s+)', input_str)

    # Capitalize the first letter of each word and join them back
    capitalized_words = [word.capitalize() if not word.isspace() else word for word in words]

    # Reconstruct the string with the capitalized words while preserving spaces
    capitalized_str = ''.join(capitalized_words) 

    return capitalized_str

# Input the string
input_str = input("Enter the string: ")

# Capitalize the names while preserving spaces and print the result
capitalized_output = capitalize_names_with_spaces(input_str)
print("Capitalized output:", capitalized_output)