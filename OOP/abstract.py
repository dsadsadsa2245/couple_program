"""Абстракция (абстрактный класс) - принцип ООП, в котором создается абстрактный класс (класс - пустышка).
То есть в котором создаются названия аттрибутов и методов, для того чтобы в дочерних классах переопределить
их нужным образом. (у них есть название, но нет логики)"""
"""abstractmethod - декоратор который требует переопределение метода в наследкемом классе.
   abstractproperty -  декоратор которрый требует переопределения аттрибутов класса
    """
from abc import ABC, abstractmethod, abstractproperty


class AbstractAnimal(ABC):
    """abstractmethod - декоратор который требует переопределение метода в наследуемом классе.
       abstractproperty - декоратор который требует переопределения аттрибутов класса
        """

    @abstractmethod
    def voice(self):
        ...

    @abstractproperty
    def legs(self):
        ...


# obj=AbstractAnimal()


class Dog(AbstractAnimal):
    legs = 4

    def voice(self):
        print("гав-гав")
class Cat(AbstractAnimal):
    legs = 4

    def voice(self):
        print("мяу-мяу")


dog = Dog()
cat=Cat()
arr=[dog,cat]
for i in arr:
    i.voice()
    print(i.legs)

# ---------------------------------------------------------------------


# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         ...
#
#
# class Square(Shape):
#     def __init__(self, lenght):
#         super().__init__('Square')
#         self.lenght = lenght
#
#     def area(self):
#         return self.lenght ** 2
#
#
# obj = Square(12)
# print(obj.area())