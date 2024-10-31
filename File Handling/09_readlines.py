# Example of using readlines() to traverse each line in a file

with open("File_04.txt", "r") as file:
    lines = file.readlines()  # Reads all lines into a list

    for line in lines:
        print(line.strip())  # strip() removes any extra newline characters