"""JSON- Java Script Object Notation"""
"""Единый текстовый формат данных,был создан для зранения и
передачи данных между сервисами"""
#<filename>.json  ---->  файл в формате JSON
"""пример JSON"""
# {
#     'id':1,
#     'author':{
#     'name':'Ed sheeran',
#     'age':35
#     },
#     'title':"don't"
#     'feat':false
# }




# !!!!!!!!!!!!!!!!!!!
# js object=={key:value}
# Py dict=={key:value}
# JSON=={key:value}

'''Процессы с реализацией и десериализацией данных(конвертация)'''



'''
сериализация(запись данных  в JSON)-это перевод из python в JSON формат

dump-записывает данные в файл формата JSON

dumps-записывает данные в текст формата JSON
'''


'''
Десереализация(чтение данных из JSONa)-это процесс перевода из JSON в python dictionary.

load-функция которая считывает данные из файла JSON

loads-функция которая считывает данные из текста JSON
'''
#__________________________________________________________
"""процесс реализации"""
"""здесь у нас есть питоновский словарь,с помощью dumps мы переводим его JSON"""
# import json
# dict_={
#     "name":"Daniel",
#     "age":15,
#     "status":True,
#     "wife":False,
#     "children":None
# }
# print(dict_,type(dict_))
# json_text=json.dumps(dict_)
# print()
# print(json_text,type(json_text))
#----------------------------------------------------------------
"""создаем файл, и записали туда прошлый словарь"""
# with open('new.json','w') as file:
#     json.dump(dict_,file,indent=4)

#-----------------------------------------------
#процесс десереализации

"""потом мы из файла берем наш JSON,переводим его в питоновский словарь используя loads"""
# import json
# with open('new.json','r') as file:
#     json_data=file.read()
# print(json_data,type(json_data))
# dict_=json.loads(json_data)
# print(dict_,type(dict_))


# import json
# with open('new.json','r') as file:
#     dict_=json.load(file)
#     print(dict_,type(dict_))


from urllib.request import urlopen
import json
import pprint as pp
url='https://randomuser.me/api/'
json_data=urlopen(url)
dict_=json.load(json_data)
pp.pprint(dict_)