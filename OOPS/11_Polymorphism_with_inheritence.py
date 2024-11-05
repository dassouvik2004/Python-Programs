# Base Class/Parent Class
class shape:
    def draw(self):
        print("Drawing a shape")

# Subclass/Child Class as it inherits from parent class
class circle(shape):
    def draw(self):
        print("Drawing a circle")

# Subclass/Child Class as it inherits from parent class
class square(shape):
    def draw(self):
        print("Drawing a square")

# Function that takes any shape object
def display(shape):
    shape.draw()

circle = circle()
square = square() 

display(circle)
display(square)