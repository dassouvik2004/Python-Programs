# Multilevel Inheritance
class Employee:
    a = 1
class Programmer(Employee):
    b = 2
class Manager(Programmer):
    c = 3

obj = Employee()
print(obj.a) # prints the 'a' attribute
#print(obj.b) # Shows an error as there is no b attribute in Employee class
obj = Programmer()
print(obj.a,obj.b) #prints the 'a' attribute of employee because programmer takes Employee inheritance and 'b' attribute in Programmer class
#print(obj.a,obj.b,obj.c)
obj = Manager()
print(obj.a,obj.b,obj.c) #print the 'a', 'b' and 'c' attribute