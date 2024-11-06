# Simple Constructor
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("Souvik Das",20)
person2 = Person("Saikat Das",31)

person1.display_info()
person2.display_info()