class Animal:
    def speak(self):
        print('издает звуки')
class Dog(Animal):
    def speak(self):
        print('гав')
class BigDog(Dog):
    def speak(self):
        print('гав-гав')
class SmallDog(BigDog):
    def speak(self):
        print('тяф тяф')
class ToyDog(SmallDog):
    def speak(self):
        print('я собака игрушка гав гав гав гав гав гав')
class RobotDog(ToyDog):
    def speak(self):
        print('электронный ряф ряф')
class BigAngryDog(BigDog):
    def speak(self):
        super().speak()
        print('гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-г')
        print('гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-г')
class Cat(Animal):
    def _meow(self):
        print('мяу')
    def speak(self):
        self._meow()
class elephant(Cat):
    def _meow(self):
        print('уууууууууууууууууууууууууууууууууууууууууууууууу')

animal = Animal()
animal.speak()
dog = Dog()
dog.speak()
big_dog = BigDog()
big_dog.speak()
small_dog = SmallDog()
small_dog.speak()
toy = ToyDog()
toy.speak()
robot = RobotDog()
robot.speak()
big_angry_dog = BigAngryDog()
big_angry_dog.speak()
cat = Cat()
cat.speak()
elephant = elephant()
elephant.speak()
def say_n_times(cat,times):
    for _ in range(times):
        animal.speak()
friend = Cat
say_n_times(friend,3)
list_of_animals = [Cat(),Dog(),BigAngryDog()]
for animal in list_of_animals:
    animal.speak()
for animal in list_of_animals:
    say_n_times(animal,5)