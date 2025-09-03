class Author:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Book:
    def __init__(self, title, author: Author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"{self.title} by {self.author.get_name()}"



a = Author("Alisher Navoiy")
b = Book("Xamsa", a)
print(b.get_info())
