class Dog:
    def __init__(self,name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog("Bunny")
my_dog2 = Dog("Bob") 


my_dog.bark()
my_dog2.bark()