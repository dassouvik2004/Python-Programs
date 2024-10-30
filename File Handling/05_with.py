f = open("File Handling/file.txt") 
print(f.read())
f.close()

#This same can be written using with statement like this:

with open("File Handling/file.txt") as f:
    print(f.read())

# you don't have to explicitly close the file