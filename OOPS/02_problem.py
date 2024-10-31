class webpage:
    def __init__(self,title,url):
        self.title = title
        self.url = url
    def display(self):
        print(f" Title: {self.title} and Url: {self.url}")


page = webpage("Google","www.google.com")
page.display()