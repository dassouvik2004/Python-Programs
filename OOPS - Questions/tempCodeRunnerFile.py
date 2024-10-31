class A:
    var = 0
    def __init__(self,value):
        A.var += 1
        self.value = value
        print("The object value is",value)
        print("The value of the class variable is",A.var)
    def __del__(self):
        A.var -= 1
        print(A.var)
        print(f"Object with value {self.value} is going out ot scope")

obj1 = A(10)
obj1 = A(20)
del obj1
# del obj1