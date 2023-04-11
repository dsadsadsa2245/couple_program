# Декоратор-функция, котопрая позволяет  без изменение кода функции расширить ее функционал
# def decorator(func):
#     print(func)
#     func()
# def decorator(func):
#     def wrapper():
#         print(f"Мы вызвали функцию; {func.__name__}")
#         func()
#
#     return wrapper
# @decorator #@decorator->decorator(hello)
# def hello():
#     print("Hello stranger!")
# @decorator
# def john():
#     print("My name is John Snow.I am the king of the north")
# hello()
# print()
# john()
# decorator(hello)
# print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
# decorator(john)

# pythonic way-@
# Синтактический сахар- красота кода
#


# import time
# def benchmark(func):
#     def wrapper():
#         start_time=time.time()
#         func()
#         finish_time=time.time()
#         print(f'Время выполнения функции: {func.__name__}, заняло: {finish_time-start_time}')
#     return  wrapper
# @benchmark
# def loop():
#     i=0
#     range_number=1
#     while i<range_number:
#         i+=1
#         #print(i)
# @benchmark
# def add():
#     i=0
#     range_number=100_000
#     ls=[]
#     while i<range_number:
#         i+=1
#         ls.append(i)
#         #print(ls)
# loop()
# add()


# def bold(func):
#     def wrapper(*args, **kwargs):
#         res = "<bold>" + func(*args,**kwargs) + "</bold>"
#         return res
#     return wrapper
# @bold
# def str_(name):
#     return name
# @bold
# def div(func):
#     def wrapper(*args,**kwargs):
#         res='<div>'+func(*args,**kwargs)+"</div>"
#         return res
#     return  wrapper
# @bold
# def name(name,last_name):
#     return  name+last_name
# print(str_('daniel'))
# print(name('DAmiele','dastan'))
# print(div("plays"))


def trace(func):
    def wrapper(*args,**kwargs):
        print(f'Trace: вызвала {func.__name__}() \n она приняла args:{args},kwargs: {kwargs}')
        original_result=func(*args,**kwargs)
        print(f'Trace:вызвала: {func.__name__}() \n она вернула : {original_result}')
        return original_result
    return wrapper
@trace
def say(name,adress):
    return  f'{name} -->{adress}'
@trace
def hello(name,lastname,country):
    return f'hello {name} {lastname} from {country}'
say("Sherlok holms",'bakery streen 221B')
print()
# hello('daniel','zhanbolotov','Kg')