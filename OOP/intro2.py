# class Human:
#     age = 0
#
#     def __init__(self, name, last_name, weight, nation):
#         self.name = f"{name} {last_name}"
#         self.weight = weight
#         self.nationality = nation
#
#     def birthday(self):
#         from random import randint
#         print(f'\nHappy birthfay, {self.name}!!!')
#         self.age += 1
#         self.weight += randint(800, 7000)
#
#     def show_info(self):
#         print(self.name,self.weight,self.nationality,self.age)
#
#
# human1 = Human("Daniel", "Zhan", 3300, "KG")
# human2 = Human("Butovskiy", "KIk", 1200, "American")
# print("After one year:")
# human1.birthday()
# human2.birthday()
# human1.show_info()
# human2.show_info()
# human1.birthday()
# human2.birthday()
# human1.show_info()
# human2.show_info()
# human1.birthday()
# human2.birthday()
# human1.show_info()
# human2.show_info()
# human1.birthday()
# human2.birthday()
# human1.show_info()
# human2.show_info()
# human1.birthday()
# human2.birthday()
# human1.show_info()
# human2.show_info()
# human1.birthday()
# human2.birthday()
# human1.show_info()
# human2.show_info()
# _________________________________________________________________-
# class Student:
#     univer='Harward'
#     def __init__(self,name):
#         self.name=name
#         self.books=[]
#         self.languages={}
#         self.knowledge=0
#         self.isreadytowork=False
#     def add_points(self,points):
#         self.knowledge += points
#         if self.knowledge>500 and not self.isreadytowork:
#             self.isreadytowork=True
#             print(f"{self.name} got 500 points!!")
#     def read_book(self,book_name):
#         self.books.append(book_name)
#         self.add_points(50)
#     def do_project(self):
#         self.add_points(100)
#     def learn_new_language(self,language,percent):
#         if percent not in range(70,101):
#             print("Набери больше очков, дурачок!")
#         else:
#             self.languages[language]=percent
#             self.add_points(percent)
# st1=Student("John Snow")
# st2=Student("Zhan Dan")
# print(st1.name)
# print(st2.name)
# print(f"Before study {st1.name}: {st1.books} {st1.languages} {st1.knowledge}")
# print(f"Ready to work: {st1.isreadytowork}")
# st1.read_book('Game of thrones')
# st1.read_book('Martin Eden')
# st1.read_book("1984")
# st1.read_book("Дюна")
# st1.do_project()
# st1.do_project()
# st1.learn_new_language('Python',40)
# st1.learn_new_language('Python',90)
# st1.learn_new_language('C++',75)
# st1.do_project()
# print(f"After study {st1.name}: {st1.books} {st1.languages} {st1.knowledge}")
# _____________________________________________________________________________________________---
# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def show_info(self):
#         return f'{self.brand} -> {self.model}'
#     def __str__(self):
#         return f'{self.brand} -> {self.model}'
# obj=Car('BMW','7 series')
# print(obj)
# obj2=Car("Lada","Sedan")
# print(obj2)
# ____________________________________________________________
import random


# class Sniper:
#     health = 100
#
#     def __init__(self, name):
#         self.name = name
#
#     def shoot(self, other):
#         other.health -= 20
#         print(f"Атаковал {self.name}")
#         print(f"У {other} осталось {other.health}")
#
#     def __str__(self):
#         return self.name
#
#
# sniper1 = Sniper('Daniel')
# sniper2 = Sniper("Dastan")
# while sniper1.health  and sniper2.health:
#     choice = random.randint(1, 2)
#     sniper1.shoot(sniper2) if choice == 1 else sniper2.shoot(sniper1)
# if sniper1.health:
#     print(f"{sniper1} won the game")
# else:
#     print(f'{sniper2} won the game')
#________________________________________________________________________________________________
# class Soda:
#     def __init__(self,ingridient=None):
#         if isinstance(ingridient,str):
#             self.ingredient=ingridient
#         else:
#             self.ingredient=None
#     def __str__(self):
#         if self.ingredient:
#             print(f'Soda made of {self.ingredient}')
#         else:
#             return 'normal gazirovka'
# gaz1=Soda("Malina")
# print(gaz1)
# mapoh=Soda(5)
# print(mapoh)
#_____________________________________________________________________________________-
from typing import  List
class TriangleChecker:
    def __init__(self,sides: List[int | float]) -> None:
        self.sides=sides
    def __str__(self):
        if not all(isinstance(x, (int,float)) for x in self.sides):
            return 'нельзя построить треугольник! Инвалид валю'
        elif any(x <= 0 for x in self.sides):
            return 'нельзя построить треугольник!инвалид'
        self.sides.sort()
        if self.sides[0]+self.sides[1] <=self.sides[-1]:
            return 'нельхя построить треугольник!Сумма меньше или равна'
        else:
            return 'мы можем построить треугольник!!!!!'
e1=TriangleChecker([10,10,10])
print(e1)
e2=TriangleChecker([1,76,6])
print(e2)