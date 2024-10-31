class student:
    stream = "Beta" # This is a class attribute
    year = 2

    @staticmethod # It will run automatically without self
    def greet():
        print("Hello, Welcome to Techno India Hooghly")

    def getInfo(self):
        print(f"Name: {self.name} Stream: {self.stream} Year: {self.year}")


souvik = student()
souvik.name = "Souvik Das" # This is an object/instance attribute
souvik.greet()
souvik.getInfo()
#student.getInfo(souvik) # We can also write like this to call getInfo method