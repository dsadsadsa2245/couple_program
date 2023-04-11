"""
встроенные функции
"""

"""Анонимная функция- lambda(обычная функция с одной особенностью,у нее нет имени).
Принимает сколько-угодно параметров, но всегда возвращает одно значение
"""
# def hello():
#     return"hello"
# print(hello())
# x=lambda : 'hello'
# print(x())


# x = lambda a, b, c: (a * b) % c
# print(x(5, 10, 6))


"""в lambda ниже degree явдяется необязательным параметром"""

# a = lambda a, b, degree=None: (a * b) ** degree if degree else a * b
# print(a(3, 5, 2))

"""my_doubler хранит в себе активированную функцию и передаем ей n со значением 2."""
# def mufunc(n):
#     return lambda num: num * n
# my_doubler = mufunc(2)
# print(my_doubler(50))

"""key говорит по какой логике сортировать, в данной функции используется len. И начинаем список с конца с помощью reverse=True"""
# list=['hello','world','mil','daniel']
# a=sorted(list, key=len, reverse=True)
# print(a)


# dict = {
#     'john': 500,
#     'tirion': 160000,
#     'tom': 150,
#     "sanchar": 20,
#     'ayana': 100000
# }
# a=dict(sorted(dict.items(),key=lambda x:x[1], reverse=True))
# print(a)


"""
map(function,iterable)-применяет к каждому элементу внутри iterable функцию,которую мы ей передаем в function,закидывая в результат те данные,
которые возвращает функция.В результате мы получаем mapobject(iterator),в котором хранятся все наши данные.Она работает как цикл for.
Dсе элементы списка присваиваются переменной x.
"""

"""сделаем так чтобы первые буквы в элментах списка стала заглавной."""
# ls = ['one', 'two', 'three', 'four']
# new_ls = list(map(lambda x: x.capitalize(), ls))
# print(new_ls)
"""or"""
# ls = ['1', '2', '3', '4']
# new_ls = list(map(int, ls))
# print(new_ls)


# names = ['john', 'aria', 'baku', 'bakberdi']
# a = list(map(lambda x: f"hello, mr/mrs {x}", names))
# print(a)


"""функция высшего порядка-функция,которая принимает в качестве аргумента другую функцию"""

"""filter(function,iterable)-применяет ко всем элементам iterable функцию, которую мы передаем и возвращает
filterobject(iterator)
только с теми значениями,для которых функция вернула True
"""
# ls = ['one', 'lili', 'oleg', 'billi', 'tirion']
# res=list(filter(lambda x: len(x)>=4,ls)) #or res=list(filter(lambda x:x if len(x)>=4 else False,ls))
# print(res)


"""
enumerate(iterable) -пронумеровывает каждый элемент внутри iterable ее собственным индексом
"""
# ls=['str1','str2','str3']
# new_list=enumerate(ls)
# print(dict(new_list))


"""
zip- она соеденяет каждый элемент итерируемых объектов между собой в тип данных tuple и возвращает его итератор.
"""
"""вывод: [(1, 100, 10), (2, 200, 20), (4, 300, 30)]"""
# ls1 = [1, 2,4,3]
# ls2 = [100, 200, 300]
# ls3=[10,20,30]
# result=list(zip(ls1,ls2,ls3))
# print(result)


"""zip для создания словарей"""
# d_keys = ['hostname', 'location', 'vendor', 'model', 'IP']
# data={'october':['bishkek_october','Gorkogo 212','Vefa','Cisko','10.255.0.12'],
#       '1may':['bishkek_1may','Jibek-jolu 212','white house','Cisko','11.255.0.12']}
# bishkek_data={}
# for k in data:
#     bishkek_data[k]=dict(zip(d_keys,data[k]))
# print(bishkek_data)


"""all(),any()"""
'''all(Iterable)-возврашает True,если все элементы итерируемого объкта внутри истина,иначе возвратить False'''
# IP='10.225.0.155'
# IP1='10.124.0y.202'
# result=all(x.isdigit() for x in IP1.split('.'))
# print(result)


'''any()-возвращает True,если хотябы один элемент истина'''
"""возвращает true так как один из них true"""
# ls=[1,3,[1,2],0]
# print(any(ls))
#
#
# """проверяем вводит ли пользователей одну их запрещнных команд"""
# ignore=['rm-rf','sudo','reset','poweroff']
# command=input("Введите команду: ")
# if any(x in command for x in ignore):
#     raise  Exception('BlockYou')
# print('It is Ok')

# ________________________________________________________________
from random import choices
from string import ascii_letters, digits, punctuation
from itertools import  repeat
# for x in repeat('str',15):"""печатает 'str' 15 раз"""
#     print(x)
symbols='_()+-@!#%'
q_pass=int(input('введите количество паролей: '))
result={
    f(choices(ascii_letters,k=15),choices(digits,k=6),choices(symbols,k=2))
    for f in repeat(lambda x,y,z:''.join(set(x+y+z)),q_pass)
}
print(result)
print(f'Quantity of passfords: {len(result)}')

from statistics import mean
avg=mean(len(x) for x in result)
print(f"Average len of passwords:{avg}")