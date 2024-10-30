f = open("file.txt")

# lines = f.readlines()
#print(lines,type(lines))

# line1 = f.readline()
# print(line1, type(line1))
# line2 = f.readline()
# print(line2, type(line2))
# line3 = f.readline()
# print(line3, type(line3))

lines = f.readlines()

#print(lines) #for all lines together
for line in lines:  
    print(line,end="") #for single line and end will remove '\n'

f.close()