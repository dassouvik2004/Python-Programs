#WAPP to check greater between two no.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: ")) 
if(a>b):
    print(f'{a} is the greatest number.')
else:
    print(f'{b} is the greatest number.')

#WAPP to check smaller between two no.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: ")) 
if(a<b):
    print(f'{a} is the smallest number.')
else:
    print(f'{b} is the smallest number.')

#WAPP to check greatest between three no.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: ")) 
c = int(input("Enter the third number: "))
if(a>b and a>c):
    print(f'{a} is the greatest number.')
elif(b>c):
    print(f'{b} is the greatest number.')
else:
    print(f'{c} is the greatest number.')

#WAPP to check smallest between three no.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: ")) 
c = int(input("Enter the third number: "))
if(a<b and a<c):
    print(f'{a} is the smallest number.')
elif(b<c):
    print(f'{b} is the smallest number.')
else:
    print(f'{c} is the smallest number.')

#WAPP to check greatest between four no.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: ")) 
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))
if(a>b and a>c and a>d):
    print(f'{a} is the greatest number.')
elif(b>c and b>d):
    print(f'{b} is the greatest number.')
elif(c>d):
    print(f'{c} is the greatest number.')
else:
    print(f'{d} is the greatest number.')

#WAPP to check whether a no is divisible by 5 or not
n = int(input("Enter any number: "))
if(n%5==0):
    print(f'{n} is divisible by 5.')
else:
    print(f'{n} is not divisible by 5.')

#WAPP to check whether a no is divisible by 3 but not 9
n = int(input("Enter any number: "))
if(n%3==0 and n%9!=0):
    print(f'{n} is divisible by 3 but not 9.')
else:
    print(f'{n} is not divisible by 3.')

#WAPP to calculate following grade system of MAKAUT.
n = int(input("Enter your marks: "))
if(n>100):
    print("Invalid marks.Please try again.\n")
else:
    if(n<=100 and n>=90):
        print("You got O grade.")
    elif(n>=80):
        print("You got E grade.")
    elif(n>=70):
        print("You got A grade.")
    elif(n>=60):
        print("You got B grade.")
    elif(n>=50):
        print("You got C grade.")
    elif(n>=40):
        print("You got D grade.")
    else:
        print("You're fail!")

#WAPP to check profit and loss of a product.
sp = int(input("Enter the selling price of your product: "))
cp = int(input("Enter the cost price of your product: "))
if(sp>cp):
    print("You're in profit!")
elif(sp==cp):
    print("You got no profit and no loss.")
else:
    print("You're in loss!")

#WAPP to check a number is a 3 digit number or not
n = (input("Enter any number: "))
if(len(n)==3):
    print(f'{n} is a 3 digit number.')
else:
    print(f'{n} is not a 3 digit number.')

#WAPP to check whether a triangle is formed or not where three sides are given.
a,b,c = map(int,input("Enter three sides: ").split())
if(a+b>c and b+c>a and a+c>b):
    print("Triangle can be formed.")
else:
    print("Triangle can't be formed.")

# Write a python program to calculate area and perimeter of a triangle where three sides are user given.
import math
a = int(input("Enter the length of side a: "))
b = int(input("Enter the length of side b: "))
c = int(input("Enter the length of side c: "))
if(a+b>c and b+c>a and a+c>b):
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    perimeter = a+b+c
    print("Area of a triangle: {:.2f}".format(area))
    print("Perimeter of a triangle: ",perimeter)
else:
    print("Triangle can't be formed.")

#WAPP to check whether a triangle is scelene, equilateral or other.
a = int(input("Enter the length of side a: "))
b = int(input("Enter the length of side b: "))
c = int(input("Enter the length of side c: "))
if(a==b==c):
    print("Triangle is a Equilateral Triangle.")
elif (a==b!=c or b ==c!=a or a==c!=b):
    print("Triangle is Isosceles Triangle.")
else:
    print("Triangle is Scalane Triangle.")