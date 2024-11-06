class Car:
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def display_info(self):
        print(f"Car: {self.make} {self.color} {self.make} {self.year}")

car1 = Car("Toyoto","Corolla",2020,"Red")
car1.display_info()