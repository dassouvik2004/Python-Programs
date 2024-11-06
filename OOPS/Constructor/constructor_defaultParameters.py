class Book:
    def __init__(self,title="Unknown",author="Unknown"):
        self.title = title
        self.author = author
    def display_info(self):
        print(f"Title: {self.title} and Author: {self.author}")

book1 = Book("Python Programming","Subrata Saha")
book2 = Book("DSA through C")

book1.display_info()
book2.display_info()