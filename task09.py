class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius   

    @property
    def celsius(self):
        return self._celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32



t = Temperature(0)
print(t.celsius)     
print(t.fahrenheit) 




