def swap(a,b):
    a,b = b,a
    return a,b
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
a,b = swap(a,b)
print("After swapping")
print("First number is",a,"and second number is",b)