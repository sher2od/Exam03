class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"


car1 = Car("Toyota", "Camry", 2020)
print(car1.get_info())
