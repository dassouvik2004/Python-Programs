string1 = input("Enter any string: ")
string1 = string1.upper()
count = 0

for char in string1:
    if char in "AEIOU":
        count += 1

print(count)