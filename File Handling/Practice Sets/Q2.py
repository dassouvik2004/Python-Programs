def sort_string_alphabetically(input_string):
    # Split the string into words
    words = input_string.split()

    # Sort the list of words alphabetically
    words.sort()

    # Join the sorted words back into a string
    sorted_string = ' '.join(words)

    return sorted_string

# Input from the user
input_string = input("Enter a string: ")

# Output the sorted string
print("Sorted words:", sort_string_alphabetically(input_string))
