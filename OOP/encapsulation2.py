"""Антоция свойств (@property(getter setter))"""


# class Person:
#     __name = 'Dan'
#     __age = 22
#     __code = '+996'
#     __number = '502040408'
#     __full_number = __code + __number
#     @property
#     def name(self):
#         """the name property"""
#         print(self.__name)
#     @name.setter
#     def name(self,value):
#         print("Setter",value)
#         if not isinstance(value,str):
#             print("Invalid value for name")
#         else:
#             print('Setter',value)
#             self.__name = value
#     @property
#     def age(self):
#         print(self.__age)
#     @age.setter
#     def age(self,value):
#         if not isinstance(value,int) or value not in range(0,150):
#             print('Invalid values')
#         else:
#             self.__age = value
#     @property
#     def number(self):
#         name=input('введите свое имя: ').lower().strip()
#         if self.__name.lower().strip() != name:
#             print("Invalid name")
#         else:
#             print(self.__full_number)
#     @number.setter
#     def number(self,value : dict):
#         """"""
#         if value['code'] !=  "+996":
#             print("номер изменился с кыргызского")
#         elif len(value['number']) != 9:
#             print('number changed from Kg num')
#         self.__code=value['code']
#         self.__number=value['number']
#         self.__full_number=self.__code+self.__full_number
# obj=Person()
# obj.name
# obj.name='Jamie'
# obj.name
# --------------------------------------------------------------------------------------------------
# class Circle:
#     def __init__(self,radius):
#         self._radius=radius
#     def _get_radius(self):
#         print("getter , _get_radius")
#         return self._radius
#     def _set_radius(self,value):
#         print("setter , _set_radius")
#         if not isinstance(value, (int,float)):
#             raise ValueError('radius must be an int or float object!')
#         self._radius=value
#     radius=property(fget=_get_radius,fset=_set_radius, doc='The radius property')
#     def _del_radius(self):
#         print('deleter ,_del_radius')
#         answer=input('Are you sure to delete radius(yes/no)?')
#         if answer.lower().strip() == 'yes':
#             del self._radius
#             print('deleted')
#         else:
#             print('not deleted')
# obj=Circle(5)
# print(obj.radius)
# obj.radius=7.5
# print(obj.radius)
# ---------------------------------------------------------------------------------------------------------"""
# class A:
#     test=5
# obj=A()
# print(obj.test)
# del A.test
# --------------------------------------------------------------------
# class CoordinateWriteError(Exception):
#     pass
#
#
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#     @property
#     def x(self):
#         print(self.__x)
#     @property
#     def y(self):
#         print(self.__y)
#     @x.setter
#     def x(self,value):
#         raise CoordinateWriteError('coordinate can\'t be changed! Only read')
#     @y.setter
#     def y(self,value):
#         raise CoordinateWriteError('coordinate can\'t be changed! Only read')
# obj=Point(42,74)
# print(obj.x)
# obj.x=55
# print(obj.x)
#-------------------------------------------------------------------------------------------
import hashlib,os
class User:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    @property
    def password(self):
        raise AttributeError('Password field is write only')
    @password.setter
    def password(self, value):
        if not isinstance(value,str):
            raise ValueError('инвалид, иди от сюда')
        salt=os.urandom(32)
        self._hashed_passsword = hashlib.pbkdf2_hmac('sha256', value.encode('utf-8'),salt,100_000)
        self.password=self._hashed_passsword


dan=User('Zhandan','secretkey')