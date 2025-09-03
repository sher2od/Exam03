class Flyer:
    def fly(self):
        return "Duck is flying"

class Swimmer:
    def swim(self):
        return "Duck is swimming"

class Duck(Flyer, Swimmer):
    pass


duck = Duck()
print(duck.fly())  
print(duck.swim())  

