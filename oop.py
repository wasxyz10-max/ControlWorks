
############################    1    ##############################

class Person:
    def __init__(self, age=None):
        self.__age = None
        if age is not None:
            self.set_age(age)

    def set_age(self, age):
        if age < 0:
            raise ValueError('Возраст не может быть отрицательным.')
        self.age = age

    def get_age(self):
        return self.age
    

p = Person()        
p.set_age(20)
print(p.get_age())  
p.set_age(-9)       



############################    2    ##############################


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} издает звук.')


class Dog(Animal):
    def speak(self):
        return 'Woof.'
    

class Cat(Animal):
    def speak(self):
        return 'Meow.'

dog = Dog('Bob')
cat = Cat('Misty')

print(dog.name, dog.speak())
print(cat.name, cat.speak())



############################    3    ##############################



class Vehicle:

    def move(vehicle):
        return "Vehicle is moving"
        

class Car(Vehicle):
    def move(car):
        return "Car is driving"
    
class Bicyclе(Vehicle):
    def move(bicycle):
        return "Bicycle is pedaling"
    
car = Car()
bicycle = Bicyclе()

print(car.move())       
print(bicycle.move())   




#############################    4    ##############################




from abc import ABC, abstractmethod



class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pi = 3.14
        return round(pi * (self.radius ** 2))

rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())   
print(circle.area()) 
 
