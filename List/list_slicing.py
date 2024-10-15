elements = [10, 20, 30, 40, 50]
print("Before slicing operation: ",end = ' ')
print(elements)

slice1 = elements[1:4]
#Extracts elements from index position 1 to 3
print("New extracted List is: ",end = " ")
print(slice1)

slice2 = elements[:4]
#Extracts element from index position 0 to 3
print("New extracted List is: ",end = " ")
print(slice2)

slice3 = elements[1:]
#Extracts element from index position 1 to end
print("New extracted List is: ",end = " ")
print(slice3)

slice4 = elements[1:4:2]
#Extracts elements from index position 1 and 3
print("New extracted List is: ",end = " ")
print(slice4)

slice5 = elements[4:1:-1]
#Extracts elements from index position 4 and 2
print("New extracted List is: ",end = " ")
print(slice5)

slice6 = elements[-1:-4:-1]
#Extracts elements from index position -1 and -3
print("New extracted List is: ",end = " ")
print(slice6)

slice7 = elements[-1:1:-1]
#Extracts elements from index position -1 and 2
print("New extracted List is: ",end = " ")
print(slice7)

slice8 = elements[-3::-1]
#Extracts elements from index position -3 to beginning of the list
print("New extracted List is: ",end = " ")
print(slice8)

slice9 = elements[:-4:-1]
#Extracts elements from end to index position -3
print("New extracted List is: ",end = " ")
print(slice9)

slice10 = elements[::-1]
#Extracts all elements but in reverse direction
print("New extracted List is: ",end = " ")
print(slice10)