with open('File_06.txt', 'r') as file:
    lines = file.readlines()

# Manipulate lines
lines = [line.upper() for line in lines]  # Convert each line to uppercase

with open('File_06.txt', 'w') as file:
    file.writelines(lines)