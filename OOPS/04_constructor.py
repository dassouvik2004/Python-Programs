class student:
    def __init__(self,name,stream,year): # This is dunder method which is automatically called
        self.name = name
        self.stream = stream
        self.year = year
        print(f"Name: {self.name} Stream: {self.stream} Year: {self.year}")
    
souvik = student("Souvik Das","BCA",2)
swopam = student("Swopam Ganguly","BBA",2)