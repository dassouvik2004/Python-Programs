elements = [10,20,30,40,10]
print("The List : ",end = " ")
print(elements)

num = int(input("Enter any number: "))
if num in elements:
    posn = elements.index(num) #Return first occurrance of num
    print("The index of 1st occurrence of %d is:"%(num),end = " ")
    print(posn)
    print("And total occurrence of %d is: %d"%(num,elements.count(num)))
else:
    print("Number not found")