# ООП-объектно ориентированное программирование

# Класс- это описание того как должен выглядеть объект,
# то есть в классе мы описываем какими свойствами(данными) и поведением(функции) должен обладать объект

# Объект-это сущность которую мы создвем от класса.У объеста есть собственные состояния свойств(данные)

# Целью создания было свзаать данные с функциями которые управляли этими данными 

# Свойтсва(аттрибуты) - называют обычные переменные внутри класса, в которых хранятся данные объекта

# Методы-это обычные функции внутри класса,мытоды описывают воведение в объекте

# class Dog:
#     name='Daniel' ----> Это у нас аттрибут
#     def dog(): ---------------------->>>>Это у нас метод
#         name ="Daniel"

# class Human:
#     age = 0
#
#     def __init__(self, first_name, last_name, job, citizenship):
#         self.name = first_name + ' ' + last_name
#         self.job = job
#         self.citizen = citizenship
#
#     def show_info(self):
#         return f'Name: {self.name}, age: {self.age}, job:{self.job}, citizen: {self.citizen}'
#     def hello(self):
#         if self.age>100:
#             return f'Офигеть ты взрослый: {self.age}'
#         else:
#             return 'сосунок'
#
# john = Human('Jon', 'Snow', 'King', 'Northerner')
# Bilal=Human("Daniel",'Zhanbolotov','student','Kyrgyz')
#
# print(john,type(john))
# print(dir(john))
# print(john.show_info())
# john.age=4
# print(john.hello())

# class Dog:
#     """атрибуты класса"""
#     age=0
#     ushi=True
#     def __init__(self,name,color):
#         """инициализатор нужен для того чтобы создавать объекты.
#         Именно здесь создаются аттрибуты объекта"""
#         """self---ссылка на объект который только что создался"""
#         self.name=name
#         self.color=color
#     def bark(self):
#         return f'{self.name} лает!!!Его цвет {self.color}.Его возраст - {self.age}.Это больше чем {self.age-1}'
# buldog=Dog(color='Rex',name='kefeteememeemememee')
# buldog.age=65
# print(buldog.bark())


class Human:
    def __init__(self):
        print("init world")
    def eat(self):
        print("eat worked")
obj=Human()
print(obj.__init__())
print(obj.eat())