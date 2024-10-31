class Employee:
    company = "Microsoft"
    def __init__(self,name,department,salary):
        self.name = name
        self.department = department
        self.salary = salary
        print(f"Name: {self.name}\n Department: {self.department}\n Salary: {self.salary}\n Company: {self.company}")

souvik = Employee("Souvik Das","Full-Stack Developer","1,20,000")
swopam = Employee("Swopam Ganguly","Frontend Developer","1,30,000")
tanmoy = Employee("Tanmoy Senapati","UI/UX","1,00,000")
sujal = Employee("Sujal Mishra","Backend Developer","90,000")