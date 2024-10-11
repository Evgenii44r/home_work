class Temperature:
    def __init__(self,celsius):
        self.__celsius = celsius
        self.__fahrenheit = celsius*1.8+32
    def get_fahrenheit(self):
        return self.__fahrenheit
temp = Temperature(25)
print(temp.get_fahrenheit())
