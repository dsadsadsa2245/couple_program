"""class methods, instance methods, static methods"""
"""instance methods - обыяные методы,которвые принимают первым аргументом self(ссылка на объект).
Нужны они чтобы внутри метода мы могшшил работать с аттрибутами объекта,получать их или изменять"""

# class Test:
#     def instance_method(self):
#         print('метод объекта')
# obj=Test()
# obj.instance_method()
# Test.instance_method(obj)
"""class methods - методы, которвые приинимают первым аргументом cls(ссылка на класс).
Нужны они для создания тлт изменения атрибутов класса и для манипуляций с классом внутри метода.
Создается при помощи декоратора  @classmethod"""


# class Test:
#     @classmethod
#     def class_method(cls,a):
#         print("метод класса")
#         print("первый аргумент:" , cls)
# obj=Test()
# print(Test,'!!!')
# print()
# obj.class_method(5)
# print()
# Test.class_method(5)

class C:
    counter = 0

    def __init__(self):
        self.a = 4
obj_1=C()
obj_2=C()
print(obj_1 .counter)
