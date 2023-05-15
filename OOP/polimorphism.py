"""функция полиморфизм -> len()"""
"""Полиморфизм - способность функции(метода) использоваться для разных типов(классов)"""
"""Широко распрастраненное определение: "один интерфейс - много реализаций\""""
# list.pop()
# set.pop()
# dict.pop()
# class Cat:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def info(self):
#         print(f"It's a cat.Cat's name is - {self.name}, age - {self.age}")
#     def make_sound(self):
#         print("Мяу, Мяу")
# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def info(self):
#         print(f"It's a dog.Dog's name is - {self.name}, age - {self.age}")
#     def make_sound(self):
#         print("Гав, гав")
# cat=Cat("TOM",4)
# dog=Dog("Rex",'6')
# for obj in (cat,dog):
#     obj.info()
#     obj.make_sound()
#-------------------------------------------------------------------------------------------------
from  math import  pi
class Shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        pass
    def fact(self):
        return f"Я фигура в двумерной плоскости: {self.name}"
class Square(Shape):
    def __init__(self,lenght):
        super().__init__('Квадрат')
        self.lenght=lenght
    def area(self):
        return self.lenght ** 2
    def fact(self):
        return super().fact() + '\nУ квадрата все стороны равны'
class Circle(Shape):
    def __init__(self,radius):
        super().__init__('Окружность')
        self.radius=radius
    def area(self):
        return pi * (self.radius ** 2)