# """Множественное наследование-это когда класс наследуется от двух и более классов"""
# 
# 
# class Auto:
#     def playmusikatstation(self):
#         print('Musik is playing')
# 
#     def ride(self):
#         print("We're riding on the ground")
# 
# 
# class Plane:
#     def playmusikatstation(self):
#         print("Listening Ed Sheeran!")
# 
#     def fly(self):
#         print("We're flying!")
# 
# 
# class FutureAuto(Auto, Plane):
#     pass
# 
# obj=FutureAuto()
# obj.ride()
# obj.fly()

"""Проблема ромба - поиск шел в родительский класс прежде
 чем искать у соседнего общего потомка (решена с помощью MRO)"""

# MRO (method resolution order)- механизм ждя корректного поиска родительских методов.
# БЫл создан для решения проблемы ромба, которая появилась после введения в python.
# Поиск идет таким образом что если у родительских классов есть общий предок, то идет поиск в ширину
# class Zero:
#     def say(self):
#         print('class Zero')
#
#
# class First(Zero):
#     def say(self):
#         print('class First')
#
#
# class Second(Zero):
#     def say(self):
#         print('class Second')
#
#
# class MyClass(First, Second):
#     def say(self):
#         super().say()
#         print('class MyClass')
# obj=MyClass()
# obj.say()
# print(MyClass.mro())
# ---------------------------------------------------------------------------
# class Z:
#     pass
# class Y:
#     pass
# class A(Z):
#     pass
# class B(Y):
#     pass
# class X(A,B):
#     pass
# print(X.mro())
# # -------------------------------------------------------------
# class Y:
#     pass
#
#
# class X:
#     pass
#
#
# class A(X, Y):
#     pass
#
#
# class B(Y, X):
#     pass
#
#
# class MyMro(type):
#     def mro(cls):
#         return [cls, A, B, X, Y, object]
#
#
# class MyClass(A, B, metaclass=MyMro):
#     pass
# print(MyClass.mro())
# ----------------------------------------------------------------------
"""Mixins
Миксины-классы которые используются для наследования и передачи дочерним классам определенных методов
для чего:
1. вы хотите предоставить множество доролнительных методов для классов
2. вы хотите использовать один конкретный метод во множестве разных классов"""


# class EnginMixin:
#     def start_engine(self):
#         print("Started engine")
# class RadioMixin:
#     def play_radio(self):
#         print("musik is playing")
# class Auto(EnginMixin,RadioMixin):
#     pass
# class Plane(EnginMixin):
#     pass
# class Smartphone(RadioMixin):
#     pass
# class Train(EnginMixin,RadioMixin):
#     pass
# -----------------------------------------------------------------------------------
class FlyMixin:
    def fly(self):
        print('I can fly!')


class WalkMixin:
    def walk(self):
        print("I can walk!")


class SwimMixin:
    def swim(self):
        print("I can swim")


class Human(WalkMixin, SwimMixin):
    name = 'Daniel'

    def talk(self):
        print('I can talk!!!')


class Fish(SwimMixin):
    name = 'Darwin'


class Exocoetidae(SwimMixin, FlyMixin):
    name = 'fly_fish'


class Duck(SwimMixin, WalkMixin, FlyMixin):
    name = 'Donald_Duck'


obj = Human()
obj.walk()
obj.swim()
