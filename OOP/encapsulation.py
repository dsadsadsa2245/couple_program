"""Инкапсуляция
1. Языковая конструкция ,которая помогает связать данные с методами для
их обратботки и управления (связь между данными и методами которые управляют ими)
2.Механизм сокрытия ,при помощи которого можно ограничить доступ одного компонента программы к другому"""

"""Инкапсуляция как связь"""
# class Phone:
#     number='+996502040408'
#     def print_number(self):
#         print(f"Мой номер: {Phone.number}")
#         print(f'МОй номер: {self.number}')
# myphone=Phone()
# myphone.print_number()
"""
Инкапсуляция как механизм сокрытия
3 уровня сокрытия данных в питоне
    1.Публичный(public) - number, print_number
    2.Защищенный(_protected) - _number
    3.Приватный(__private) - __number
"""


# class Car:
#     _country='German'
#     def __init__(self):
#         self.marka='Mercedes-Benz'
#         self.model='w140'
#         self.__color='gray'
# obj=Car()
# print(dir(obj))
# print(obj._Car__color)
# print(4)

# class Phone:
#     username='Dan'
#     caller='Nurs'
#     count_of_calls=15
#     def call(self):
#         print(f'{self.caller} звонит вам!')
#         question = input('взять трубку(yes\\no):')
#         if question.lower().strip() == 'yes':
#             self.__turn_on()
#         else:
#             print("Сбросил трубку")
#     def increment_calls(self):
#         self.count_of_calls += 1
#     def __turn_on(self):
#         self.increment_calls()
#         print('Aloo!')
#         print(f'Count of calls with {self.caller}: {self.count_of_calls}')
# dan=Phone()
# dan.call()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f'My name is {self.name} and I\'m {self.age} years old!')


obj = Person('Dan', 15)
obj.display_info()
obj.nationality = 'American'
print(obj.nationality)
obj.age = -15
obj.name = 555555555
obj.display_info()
"""------------------------------------------------------------------------------------------------------------"""
# getter & setter
"""онинужны чтоююы избежать прямого обращения к сокрытым атрибутам
при этом можно добавить логику валидации (проверки) данных которым будут установлены в атрибут"""


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display_info(self):
        print(f'My name is {self.__name} and I\'m {self.__age} years old!')
    """getter"""
    def name(self):
        return self.__name
    def age(self):
        return self.__age
    """setter"""
    def set_age(self, age):
        if not isinstance(age, str) or not 0 <= age < 150:
            print("Name must be str object")
        else:
            self.__age = age


obj = Person('Dan', 15)
print(obj.name())
obj.set_age(5)
obj.age()
