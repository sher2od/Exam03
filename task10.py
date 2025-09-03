class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name}, {self.age} years old"


class Employee(Person):
    def __init__(self, name, age, company):
        super().__init__(name, age)   
        self.company = company

    def get_info(self):
        return f"{super().get_info()}, works at {self.company}"


e = Employee("Ali", 19, "Epam")
print(e.get_info())
