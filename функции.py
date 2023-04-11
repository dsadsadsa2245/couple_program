# найти квадрат,куб, результат деления на сто
# num1=5
# -> {'2':25,'3':125,'100':0.05}
num1 = 5
num2 = 16
num3 = 28
num4 = 1154
num5 = 31


# print({'num': num1, '2': num1 ** 2, '3': num1 ** 3, '100': num1 / 100})
# print({'num': num2, '2': num2 ** 2, '3': num2 ** 3, '100': num2 / 100})
# print({'num': num3, '2': num3 ** 2, '3': num3 ** 3, '100': num3 / 100})
# print({'num': num4, '2': num4 ** 2, '3': num4 ** 3, '100': num4 / 100})
# print({'num': num5, '2': num5 ** 2, '3': num5 ** 3, '100': num5 / 100})
# ___________________________________________________________________________________--------______---
# Функция- это именнованая часть программы,которая содержит в себе определенный набор инструкций,
# и может вызываться в других частях программы столько раз скольк угодно

# Параметры функции- переменные которые будут принимать данные от пользователя,и хранить в себе эти данные

# Аргументы функции- данные которые мы передаем в функцию,в моменте вызова
# _______________________________________________________________________________________________________
# *args, **kwargs в функциях
# def printscores(students,*args):
#     print(f'name of student: {students}')
#     print(args)
# print(printscores("daniel",10,90,80,95,88))
# def printPetNames9(owner,**pets):
#     print(owner)
#     print(pets)
#     # for pet,name in pets.items():
#     #     if type(name)==list:
#     #         print(f'{pet}:',*name)
#     #     print(f'{pet}:{name}')
# printPetNames9('Daniel',dog="pluto",cat="Tom",fish=['nemo,dori,badya'],turtle='Leonardo')


# def iseven(num:int) -> bool:
#     """return True if num is even, if odd return False"""
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# print(sum([1,23,345]))
#     # return  True if num%2==0 else False
#
#
# print(iseven(7))
# def calc(num1, num2, operation):
#     if operation == '-':
#         return     def add_(num1, num2):
#         return num2 + num1
#
#     def sub_(num1, num2):
#         return num1 - num2
#
#     def div_(num1, num2):
#         return num1 / num2
#
#     def mult_(num1, num2):
#         return num1 * num2
#     if operation == '/':
#         return div_
#     if operation == '*':
#         return mult_
#     else:
#         return add_
#
#
# positive=4525
# negative=-3425
#
#
# print(calc(5, 5, "+"))
