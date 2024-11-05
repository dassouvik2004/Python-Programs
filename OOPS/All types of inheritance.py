class Employee:
    def __init__(self,name):
        self.name=name
    def work(self):
        return f"{self.name} working."
class Manager(Employee):
    def manage(self):
        return f"{self.name} managing."
class Coding:
    def code(self):
        return "Writing code."
class Designing:
    def design(self):
        return "Creating Design."
class Developer(Employee,Coding):
    def develop(self):
        return f"{self.name} developing a software."
class Intern(Manager):
    def assist(self):
        return f"{self.name} assisting."
class LeadDeveloper(Developer,Designing):
    def lead(self):
        return f"{self.name} is leading."
#SINGLE INHERITANCE
manager = Manager("Sujal")
print(manager.work())
print(manager.manage())
#Multiple Inheritance
developer = Developer("Sujal")
print(developer.work())
print(developer.develop())
#Multilevel Inheritance  /  Hybrid Inheritance
lead_dev = LeadDeveloper("Sujal")
print(lead_dev.work())
print(lead_dev.develop())
print(lead_dev.code())
print(lead_dev.design())
print(lead_dev.lead())
#Hierarchical Inheritance
intern = Intern("Sujal")
print(intern.work())
print(intern.manage())
print(intern.assist())