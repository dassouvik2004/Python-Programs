input_string = "Hello my BCA Friends."
uppercase_string = ""
for char in input_string:
    if char.isupper():
        uppercase_string = " ".join([uppercase_string,char])

print("Only uppercase lettes are:",uppercase_string)