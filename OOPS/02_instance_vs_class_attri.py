class student:
    stream = "Beta" # This is a class attribute
    year = 2

souvik = student()
souvik.name = "Souvik Das" # This is an object/instance attribute
print(f"Name: {souvik.name} Stream: {souvik.stream} Year: {souvik.year}")

swopam = student()
swopam.name = "Swopam Ganguly" # This is instance attribute
swopam.stream = "BBA" #Instance attribute takes more preference than class attribute so that will print
print(f"Name: {swopam.name} Stream: {swopam.stream} Year: {swopam.year}")

# Here 'name' is the object/instance attribute and 'stream' & 'year' are the class attributes as they directly belong to the class