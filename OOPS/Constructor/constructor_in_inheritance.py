class Animal:
    def __init__(self,name):
        self.name = name
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    
    def display_info(self):
        print(f"Name: {self.name}, Breed: {self.breed}")

dog1 = Dog("Buddy","Golden Retriever")
dog1.display_info()