def counts(string1):
    vowels = ['a','e','i','o','u']
    vowels_count = [0,0,0,0,0]

    string1 = string1.lower()

    for char in string1:
        if char in vowels:
            index = vowels.index(char)
            vowels_count[index]  += 1
    
    for i in range(len(vowels)):
        print(f"Number of '{vowels[i]}': {vowels_count[i]}")

string1 = input("Enter a string: ")

counts(string1)