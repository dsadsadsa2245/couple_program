# 2.
# a = 0
# b = 2
# c = 5
# c = a + b + c 
# print()
# a = a + b
# b = c - b
# print(a, b, c)

# #5 
# a = [1,2,3,4]
# a 
# print(a)

# 4

# a = 33541
# if a%2 == 0 and len(str(a)) == 5:
#     b = list(a)
#     if b[2] % 2 == 0 and b % 4 ==0:
#         print(a)
#     else:
#         print("no")

# 5
# 6 
# geo_logs = []
# geo_logs = geo_logs.copy()
# geo_logs = [v for v in geo_logs if v[1][1] == 'Росиия']
# print(geo_logs)
# 1
# def find(a):
#     perimetr=a*4
#     area=a**2
#     diogonal=((a**2)*2)**0.5
#     return f"{perimetr},{area},{diogonal}"

# print(find(5))
# 3
# a=5643
# a=str(a)
# if a[0]>a[1] and a[1] > a[2] and a[2] > a[3]:
#     print("yes") 
# else:
#     print("no")

# 7. 

# x = 1
# a = 30

# y = int(input())
# k = int(input())

# print(f'{y * a} рублей')

# print(f'{k / a} килограм')

# 8

# for i in range(1, 51):
#     if i % 3== 0:
#         print('Fizz')
#     if i % 5 == 0:
#         print('Buzz')
#     if i % 3 == 0 and i % 5 ==0:
#         print('FizzBuzz')

# a = 3712
# b = list(a)
# b = sorted(b)
# c = int(b[-1]+b[:-1]+b[0])
# print(c)

# 9
# number = 459  # Заданное трехзначное число
# reversed_number = 0  # Переменная для хранения перевернутого числа
#
# while number > 0:
#     digit = number % 10  # Получаем последнюю цифру числа
#     reversed_number = reversed_number * 10 + digit  # Добавляем цифру в перевернутое число
#     number = number // 10  # Удаляем последнюю цифру из исходного числа
#
# print(reversed_number)  # Выводим перевернутое число
# --------------------------------------------------------------------------
# step = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# list1 = [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ]
# a = [list_[x] for x in range(0, len(list_) + 1, step)]
# b = [list_[x] for x in range(1, len(list_) + 1, step)]
# for element in b:
#     if element in list_:
#         list_.remove(element)
# for element1 in a:
#     if element1 in list_:
#         list_.remove(element1)
# gh=[a,b,list_]
# print(gh)
# -----------------------------------------------------------------
# list_ = ['sun', 'flowers', 'rumor',
# 'stranger', 'adventure', 'architect', 'accompany',
# 'abandon', 'cartoon']
# ls=[]
# a=input()
# for x in list_:
#     if x[0]==a:
#         ls.append(x)
# print(ls)
# ----------------------------------------------------
"""
example_dictionary.clear() - очищает словарь example_dictionary.

example_dictionary.copy() - возвращает копию словаря example_dictionary.

dict.fromkeys(seq[, value]) - создает словарь с ключами из seq (seq -- это последовательность в виде кортежа, списка, строчного значения, или множества) и значением value (по умолчанию None).

example_dictionary.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).

example_dictionary.items() - возвращает пары (ключ, значение).

example_dictionary.keys() - возвращает ключи в словаре.

example_dictionary.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).

dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.

dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ с значением default (по умолчанию None).

dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).

dict.values() - возвращает значения в словаре.

Метод clear() - удаляет все элементы словаря, но не удаляет сам словарь. В итоге остается пустой словарь:
"""

# Создайте класс ToDo, с аттрибутом экземпляра класса, в виде словаря todos = {}.
#
# У класса должен быть один метод set_deadline, который принимает дату дедлайна (в виде "31/12/2021") и возвращает количество дней оставшихся до дедлайна.
#
# Также, класс ToDo должен наследоваться от четырех миксинов: CreateMixin, DeleteMixin, UpdateMixin, ReadMixin:
#
# в классе CreateMixin определите метод create, который принимет в себя задачу todo и ключ key по которому нужно добавить задачу в словарь todos, если ключ уже существует верните "Задача под таким ключём уже существует".
#
# класс DeleteMixin должен содержать метод delete, который удаляет задачу по ключу key, который передается как аргумент, и возвращает сообщение 'удалили название задачу', где вместо слова название должно быть название задачи.
#
# класс UpdateMixin должен содержать метод update, который принимает в себя ключ key и новое значение new_value и заменяет задачу под данным ключом на новое значение.
#
# класс ReadMixin должен содержать метод read, который возвращает отсортированный список задач."""
# --------------------------------------------------------------------
# class CreateMixin:
#     def create(self, task, key):
#         for a in self.todos.keys():
#             if a == key:
#                 print("Задача с таким ключом уже существует")
#                 return ''
#         self.todos[key] = task
#         print(self.todos)
#
#
# class DeleteMixin:
#
#     def delete(self, keyse):
#         self.todos.pop(keyse)
#         print(f"Задача {keyse} была удалена.Новый список:")
#         print(self.todos)
#
#
# class UpdateMixin:
#     def update(self, key, new_task):
#         self.todos[key] = new_task
#         print("Список обновлен!Вот новый: ")
#         print(self.todos)
#
#
# class ReadMixin:
#     def read(self):
#         a = sorted(self.todos.items())
#         print(dict(a))
#
#
# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     todos = {}
#
#     def set_deadline(self, date):
#         """с использованием гугла.Я ничего не помню про datetime.strtime"""
#         from datetime import datetime
#         target_date = datetime.strptime(date, "%d/%m/%Y")
#         now = datetime.now()
#         left_days = (target_date - now).days
#         if left_days<0:
#             print(f"Это уже прошло, не вернуть прошлого.Сейчас: {now}")
#         else:
#             print(f"Осталось столько,работай : {left_days}")
#
# a = ToDo()
# a.create(1, 1)
# a.create(2, 2)
# a.update(1, 80)
# a.read()
# a.set_deadline('31/12/2021')


# a.create('vfrg','gbertg')
# a.create('fgrt','gbertg')
# 2) Создайте классы Dog и Cat с одинаковым методом voice.
#
# Для собак он должен печатать "Гав", для кошек "Мяу".
#
# Объявите для каждого из классов по экземпляру, для класса Cat экземпляр в переменной barsik, а для Dog экземпляр rex.
#
# Затем, вне класса объявить функцию to_pet(), которая будет принимать животное и вызывать у него метод voice().
#
# Ввод:
#
# to_pet(barsik)
# to_pet(rex)
# Вывод:
#
# Мяу
# Гав
from abc import ABC, abstractmethod, abstractproperty


# 3) Создайте классы Mercury, Venus, Jupiter, которые наследуют метод __init__ от родительского класса Planet. У объектов данного класса должен быть аттрибут orbit, орбита в классе Venus состовляет 225 земных дней, Mercury 88 земных дней, а на Jupiter 12 дней. У всех этих классов должен быть метод get_age, принимающий возраст в переменную earth_age и расчитывающий ваш возраст на данной планете.
# Метод должен возвращать возраст на Mercury в годах, на Venus в днях и на Jupiter в часах. Например, если возраст earth_age равен 20:
#
# !!!!!
# обязательное условие: создание абстрактного метода
# !!!!!
# list_ = ['hello', 23, 56, 'world',
# 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
# dict_={}
# a=sorted(list_,key=str)
# z=0
# from functools import reduce
# while z!=6:
#     z += 1
#     xc=reduce(lambda a,b)
# print(a)
# def filter_comment(comment:str,banlist=[]) -> None:
#     comment=comment.lower()
#     from string import punctuation
#     symbols=list(punctuation)
#     a=list(filter(lambda x: True if x not in symbols else False,comment))
#     print(a)
# filter_comment('привет,тпавое творчество говно!',banlist=['тупой','баран','твое','говно'])
# def filter_comment(comment: str, banlist=[]) -> None:
#     # Удаление лишних символов из комментария
#     filtered_comment = ''.join(c.lower() for c in comment if c.isalpha() or c.isspace())
#     print(filtered_comment)
#
#     # Разделение комментария на отдельные слова
#     words = filtered_comment.split()
#
#     # Проверка каждого слова на наличие в списке запрещенных слов
#     for word in words:
#         if word in banlist:
#             raise ValueError(
#                 "Ваш комментарий отправлен на перепроверку, так как, возможно, содержит неблагоприятный контекст")
#
#
# # Примеры использования
# try:
#     filter_comment('Hello, world', ['hello'])
#     print("Комментарий не содержит запрещенных слов")
# except ValueError as e:
#     print(str(e))
#
# try:
#     filter_comment('HelloWorld', ['hello'])
#     print("Комментарий не содержит запрещенных слов")
# except ValueError as e:
#     print(str(e))
#
# try:
#     filter_comment('ochocientos ochenta y ocho')
#     print("Комментарий не содержит запрещенных слов")
# except ValueError as e:
#     print(str(e))
#
# try:
#     filter_comment('I love this recipe', ['hate', 'unlike', "liken't"])
#     print("Комментарий не содержит запрещенных слов")
# except ValueError as e:
#     print(str(e))
#
# try:
#     filter_comment('Dis? recipe. is i !!UNLike!?!! really much!', ['hate', 'unlike', "liken't"])
#     print("Комментарий не содержит запрещенных слов")
# except ValueError as e:
#     print(str(e))
# -----------------------------------------------
# Dollar.
# Создайте функцию dollarize, которая принимает дробное число (float) и переводит его в
# долларизованный формат:
# dollarize(123456.78901) -> "$123,456.80"
# dollarize(-123456.7801) -> "-$123,456.78"
# dollarize(1000000) -> "$1,000,000"
# Создайте класс MoneyFmt, который содержит один единственный атрибут amount и 4 метода:
# init - инициализирует значение атрибута amount
# update - задаёт объекту новое значение amount
# repr - возвращает значение float
# str - метод, который реализует логику функции dollarize()
# //Вывод должен выглядеть следующим образом:
# cash = MoneyFmt(12345678.021)
# print(cash) -- выводит "$12,345,678.02"
# cash.update(100000.4567)
# print(cash) -- выводит "$100,000.46"
# cash.update(-0.3)
# print(cash) -- выводит "-$0.30"
# repr(cash) -- выводит -0.3

# def dollarize(num):
#     num=round(num,2)
#     numdigit=str(num).split(".")[0]
#     numfloat=str(num).split(".")[1]
#     numfg=numdigit
#     if len(numdigit)%3==0:
#         while len(numdigit)!=0:
#             numfg=numfg.replace(numfg[:3],'')
#             numdfdgs=[x for x in numdigit]
#             numdfdgs.insert(3)
#
#
# dollarize(123456789.021956546534)
# class MyString(str):
#     def __init__(self,snhg):
#         self.snhg=snhg
#     def append(self, string):
#         self.snhg = self + string
#
#     def pop(self):
#         popped_char = self[-1]
#         self = self[:-1]
#         return popped_char
#
#
# # Примеры использования
# example = MyString('Strif')
# example.append('hello')
# print(example.snhg)  # 'Stringhello'
# print(example.pop())  # 'o'
# print(example)  # 'Stringhell'
# def collect_all_possibles(list_: list, num: int) -> list:
#     list1 = []
#     for x in list_:
#         if isinstance(x, list):
#             list_help = []
#             for d in x:
#
#                 if isinstance(d,str):
#                     fghj=d*num
#                     list_help.append(fghj)
#                 else:
#                     add = d + num
#                     list_help.append(add)
#                     min = d - num
#                     list_help.append(min)
#                     mul = num * d
#                     list_help.append(mul)
#                     div = d // num
#                     try:
#                         div = d // num
#                         list_help.append(div)
#                     except Exception:
#                         pass
#                     list_help.append(div)
#                     square = d ** num
#                     list_help.append(square)
#             list1.append(list_help)
#         elif isinstance(x,str):
#             for df in range(0,num):
#                 dfg=x*num
#                 list1.append(dfg)
#         else:
#             add = x + num
#             list1.append(add)
#             min = x - num
#             list1.append(min)
#             mul = num * x
#             list1.append(mul)
#             div = x // num
#             try:
#                 div = x // num
#             except Exception:
#                 pass
#             list1.append(div)
#             square = x ** num
#             list1.append(square)
#     return list1
#
#
# print(collect_all_possibles(['hello',[8,'hellovojgrtkhnrthl',7]], 2))
users = [
  { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
  { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
  { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
  { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
  { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
]
def func15():
  for x in users:
    if "IT" in x['work']:
      print("danieo")
func15()