#f1 = open("File_1.txt","x") # Create a file using 'x' mode

#f1 = open("File_1.txt","w") # Read the file

#f1 = open("File_1.txt","r+") # Read then Write using 'r+' mode

#f1 = open("File_1.txt",'w+') # Write then read using 'w+' mode

#f1 = open("File_1.txt",'a') # append whatever you write but can't read

# f1 = open("File_1.txt","a+") #Append whatever you write and read also

# # print(f1.tell())
# # data = f1.read() // Storing somewhere
# # f1.write("Hi Welcome")
# # print(f1.tell()) #Telling the position of the file pointer
# # f1.write("This is a file")
# # print(f1.tell()) 
# # f1.seek(0) # Move the file pointer from any position to any position
# # print(f1.tell())
# # data = f1.read()
# # print(data)
# # print(f1.tell()) 
# # f1.close()
# print(f1.tell())
# #f1.write("Hi, I am back!")
# f1.seek(0)
# print(f1.tell())
# print(f1.read())
# print(f1.tell())
# f1.write("I have nothing to say")
# print(f1.tell())
# f1.seek(0)
# print(f1.read())
# print(f1.tell())

f1 = open("Ashwin.jpg","rb")
f2 = open("Ashwin_2.jpg","wb")
for i in f1:
    f2.write(i)
# print(f1.read())