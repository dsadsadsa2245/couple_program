# Область видимости и пространства имен (scoprs)
# Технология которая определяет контекст имени(переменные) в рамках которого мы можем ее использовать
# built-ins (Встроенная область видимости) -> print,len(),max()
# global(Глобальная) -> область одного файла
# enclosed(не локальная(замкнутая), nonlocal)
# local(локальная) -> область внутри одной функции
x = 200

#
# def myFunc():
#     print(x)
#     a = 300
#     print(a)
#
#
# myFunc()
# print(x)
# a=10
# def hello():
#     a='hello,world!'
#     print(a,'local inside in func')
# hello()
# print(a)
# max()

# LEGB-local enclosed global buils-in
# _______________________________________________________________________
# Enclosed
# замкнутое протранство имен-локальное протсранство, у которго есть внутренее(вложенное) локальное пространство


# global -> позволяет изменять значение глобальной перемнной находясь внутри локальной области
# nonlocal->позволяет изменять значение не локальной переменной находясь внутри локальной области
# locals-функция которая возвращает все имена внутри глобальной области видимости и локальности
# globals-func которая возвращает все имена внутри глобальной области видимости

# var=100
# def increment():
#     global var
#     var+=1 #выдает ошибку
# print(var)
# increment()
# print(var)


#
#
# c = counter()
# print(c())
# print(c())
# print(counter())
# print(counter())
# print(counter())
# print(counter())
# print(counter())
# print(counter())
# print(counter())
# print(counter())
# print(counter())
# def statistic(heroes, mobs):
#     print()
#     print(f"Ты убил: \n {heroes} героев и такое кол-во мобов: {mobs}")
#     print()
#
#
# def counter():
#     num = 0
#
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#
#     return increment
# counter_heroes=counter()
# counter_mobs=counter()
# heroes=0
# mobs=0
# while True:
#     print("Тебе доступны следующие действия: ")
#     print('1-убить героя,2-убить моба, 3-просмотреть статистику,4-выйти из игры')
#     choise=input("Введите что вы хотите сделать: ").strip()
#     if choise=="1":
#         counter_heroes()
#         heroes+=1
#     if choise=="2":
#         counter_mobs()
#         mobs+=1
#     elif choise=="3":
#         statistic(heroes,mobs)
#     elif choise=="4":
#         print("ждем еще раз")
#         break
#     else:
#         print("пожалуйста.Введите только 1 или 2 или 3 или 4")
