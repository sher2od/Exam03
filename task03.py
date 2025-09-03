class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"This is an animal named {self.name}"



class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # ota classning __init__ metodini chaqirish
        self.breed = breed

    def bark(self):
        return f"{self.name} says: Woof! Woof!"



dog1 = Dog("Buddy", "Labrador")

print(dog1.info())   
print(dog1.bark())   
