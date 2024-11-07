class Employee:
    def __init__(self,name,salary):
        self.name = name         # Public Attribute 
        self._department = "HR"  # Protected Attribute
        self.__salary = salary   # Private Attribute
    def get_salary(self):
        return self.__salary
    def set_salary(self,amount):
        if amount>0:
            self.__salary = amount
        else:
            print("Invalid salary amount.")
emp = Employee("Souvik Das",50000)

print(emp.name) # Output:Souvik

print(emp._department) # Output: HR

print(emp.get_salary()) # Output: 5000

emp.set_salary(55000) 
print(emp.get_salary()) # Output: 5500