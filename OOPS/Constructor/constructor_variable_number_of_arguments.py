class Student:
    def  __init__(self,name,*subjects):
        self.name = name
        self.subjects = subjects
    
    def display_info(self):
        print(f"Student: {self.name}")
        print("Subjects:",", ".join(self.subjects))

student1 = Student("Souvik Das","Python","DSA","Management")
student1.display_info()
student2 = Student("Sampita Das","Psychology","Education","Bengali")
student2.display_info()