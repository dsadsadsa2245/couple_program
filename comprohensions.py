# list comrehensions - генераторы списков
# list comrehensions - упрощенный подход к созданию списков , который задействует в себе цикл for,
# а так же конструкцию if для определения того,что в итоге попадет в наш список
# list -> 0-200 -> num%2 ==0
# ls=[]
# for x in range(0,201):
#     if x%2=0
#         ls.append(x)
# print(ls)
""""""
# ls=[x for x in range(0,201) if x%2==0]
# print(ls)

# #list: 0 - 300 -> num%2==0, num%3==0
# ls=[]
# for x in range (0,301):
#     if x%2== 0 and x%3==0:
#         ls.append(x)
# print(ls)

# ls=[input() for i in range(1,10) if i%3==0]
# ls = [i for i in range(1, 300) if i % 2 == 0 and i % 3 == 0]
# print(ls)

# list: 0-100 -> x%2==0: x**2 x%3==0:x**3
# ls=[]
# for x in range(0,101):
#     if x%2==0:
#         ls.append(x**2)
#     elif x%3==0:
#         ls.append(x**3)
# print (ls)

# ls = [x for x in range(0, 101) if x % 2 == 0 or x % 3 == 0]
# print(5 if input() == 'yes' else 7)

# ls = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(0, 101) if x % 2 == 2 or x % 3 == 0]
# print(ls)
# #_________________________________________________________________________________________________________--

# newlist=[expression for item in iterable <if condition ==True>]
# ls=[str(i*2) for i in range(0,11)]
# print(ls)
""""""
# ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# res = []
# for x in ls:
#     for item in x:
#         res.append(item)
# print(res)

# ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# res = [item for x in ls for item in x]
# print(res)
# ______________________________________________________________
from datetime import datetime

start = datetime.now()
# ls=[]
# for x in range(0,100_000_000):
#     ls.append(x)

# finish = datetime.now()
# ls = [x for x in range(0, 100_000_000)]
# print(finish - start)

# #__________________________________________________________

# set comprehensions
# set_ = {x for x in range(1, 100)}
# print(set_, type(set_))

# _______________________________________________________________________________________

# dict comprehensions
# dict={
#     key:value,
#     key:value
#
# }
# dict_={x:x**2 for x in range(0,16)}
# print(dict_)

# names=['Daniel','Dastan','Dalil','Beka','Nurs']
# dict={x:names.index(x) for x in names}
# print(dict)

# _____________________________________________________________________________
# dict1 = {
#     'Daniel': {'history': 99, 'fizik': 95, 'math': 94},
#     'Beka': {'history': 44, 'fizik': 75, 'math': 68},
#     'Atay': {'history': 100, 'fizik': 90, 'math': 87},
# }
# res = {}
# # for key, value in dict1.items():
# #     for inner_key, inner_value in value.items():
# #         if max(value.values()) == inner_value:
# #             res[key] = inner_key
# # print(dict1)
# # print(res)
#
# # res={key:inner_key for key,value in dict1.items()
# #                        for inner_key,inner_value in value.items()
# #                            if inner_value==max(value.values())}
# # print(res)

a='Hello,world!'
print(a[:2])