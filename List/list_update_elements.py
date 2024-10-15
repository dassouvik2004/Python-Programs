elements = [10,20,30,40,10]
print("Before updation: ",end=" ")
print(elements)

elements[2] = 55
print("After updating element of index position 2: ")
print(elements)

elements[1:4] = [22,33,44]
print("After updating from index position 1 to 3: ")
print(elements)

elements[1:3] = [55,66,77]
print("Updating index position 1 & 2 by 3 elements: ")
print(elements)