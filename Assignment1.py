# Write a python program to create a basic calculator
"""a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("The addition of the numbers:",a+b)
print("The subtraction of the numbers:",a-b)
print("The multiplication of the numbers:",a*b)
print("The divison of the numbers:",a/b)"""

# Write a python program to swap two variables(using 3rd variable)
"""a = int(input("Enter the first variable: "))
b = int(input("Enter the second variable: "))
print("Before Swapping:",a,b)
temp = a
a = b
b = temp
print("After Swapping:",a,b)"""

# Write a python program to swap two variables(without using 3rd variable)
"""a = int(input("Enter the first variable: "))
b = int(input("Enter the second variable: "))
print("Before Swapping:",a,b)
a = a + b
b = a - b
a = a - b
print("After Swapping:",a,b)"""

# Write a python program to swap two variables(using special feature of python)
"""a = int(input("Enter the first variable: "))
b = int(input("Enter the second variable: "))
print("Before Swapping:",a,b)
a,b = b,a
print("After Swapping:",a,b)"""

# Writw a python program to swap three numbers
"""a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
print("Before Swapping:",a,b,c)
a,b,c = c,b,a
print("After Swapping:",a,b,c)"""

# Write a python program to calculata area and perimeter of a circle.
"""import math
r = float(input("Enter the radius: "))
area = math.pi * r**2
perimeter = 2*math.pi*r
print("Area of a circle: ",area)
print("Perimeter of a circle: ",perimeter)"""

# Write a python program to calculata area and perimeter of a rectangle.
"""import math
l = float(input("Enter the length of the rectangle: "))
w = float(input("Enter the width of the rectangle: "))
area = l * w
perimeter = 2 * (l + w)

print("Area of the rectangle: ",area)
print("Perimeter of the rectangle: ",perimeter)"""

# Write a python program to calculate area and perimeter of a triangle where three sides are user given.
'''import math
a = int(input("Enter the length of side a: "))
b = int(input("Enter the length of side b: "))
c = int(input("Enter the length of side c: "))
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
perimeter = a+b+c
print("Area of a triangle: ",area)
print("Perimeter of a triangle: ",perimeter)'''

# Write a python program to calculate volume and surface area of a sphere.
"""import math
r = float(input("Enter the radius: "))
volume = (4/3)*math.pi*r**3
surfaceArea = 4*math.pi*r**2
print("Volume of a sphere: ",volume)
print("Surface area of a sphere: ",surfaceArea)"""
