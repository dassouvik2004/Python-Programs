element = [10,20,30,40,10,50,60,70]
print("Before removing: ", end = " ")
print(element)
del element[2]
print("After deleting element of index position 2: ",element)

element.remove(10)
print("After deleting the first occurance of 10: ",element)

num = element.pop()
print("Popping element is: ",num)
print("After popping without argument: ",element)

num = element.pop(0)
print("Popping element is: ",num)
print("After popping element of index position 0: ",element)

element[1:3] = []
print("After removing element of index position 0 and position 2: ",element)

element.clear()
print("After removing all existing elementS: ",element)