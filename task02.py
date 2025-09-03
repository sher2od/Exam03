class Student:
    def __init__(self,name,age,level):
        self.name = name
        self.age = age
        self.level = level
    
    def introduce(self):
        return f"My name is {self.name},I am {self.age} years old,studying in {self.level}nd course"
    
student1 = Student("Dilshod",20,2)
print(student1.introduce())    