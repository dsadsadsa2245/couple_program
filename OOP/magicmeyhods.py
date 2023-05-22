"""magic methods (магические методы)
dunder methods ( double underscore) -> __init__
Магия закдючается в том что эти методы запускаются без прямого обращения к ним,
определенные методы могут отвечать за определенные операторы"""
# __eq__(self,other) -> 5 == 8
#                       5.__eq__(8)
# __ne__ -> !=
# __lt__ -> <
# __gt__ -> >
# __le__ -> <=
# __ge__ -> =>
# class Word(str):
#     def __new__(cls,obj):
#         print(cls,'!!!!!!!!!!!')
#         print(obj,'!!!!!!!!!!!!!!!!!!1')
#         obj=obj.replace(' ','')
#         return super().__new__(cls,obj)
#     def __gt__(self, other):
#         print("заработал gt")
#         print(self)
#         print(other)
# obj=Word('trh')
# obj1=Word('M ackdmpd grlg egrtgewr-gt          to hjthprig')
# # obj > obj1
class Singleton:
    _instance=None
    def __new__(cls):
        if not cls._instance:
            cls._instance=super().__new__(cls)
        return cls._instance
    def __str__(self):
        return str(id(self))
a=Singleton()
b=Singleton()
print(a)
print(b)
print(a is b)