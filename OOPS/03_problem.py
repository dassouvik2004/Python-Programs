class calculator:
    def __init__(self,n):
        self.n = n
    @staticmethod
    def greet():
        print("Hello, I am solving the problem of square,cube & squareroot of a given number -")
    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The square is {self.n*self.n*self.n}")
    
    def squareroot(self):
        print(f"The square is {self.n**1/2}")

a = calculator(10)
a.greet()
a.square()
a.cube()
a.squareroot()