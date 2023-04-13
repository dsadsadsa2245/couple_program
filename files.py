# работа с файлами

# каретка - указатель - курсор

# open(<путь до файла>)
# file = open('/home/user/Desktop/ev.28/lecture/files.py') # абсолютный путь
# file = open('files.py') # относительный путь (относительно той директории в которой вы работаете

# Режимы работы с файлами
# 1. чтение -> r/r+ (read)
# 2. записи -> w/w+ (write)
# 3. добавление -> a/a+ (append)
# b,x,t


# file = open("text.txt", 'r')
# print(file.read())
# file.close

# file=open('text.txt')
# data=file.read()
# data=data.split('\n')
# print(data)
# file.close()
#


"""Контекстный менеджер"""
"""после двоеточия мы должны писать код с одной табуляцией,чтобы выйти из файла можно просто не прописывать 4 пробела"""
# with open('text.txt') as file:
#     data=file.readline()
#     print(file.read())
#     print(data)
#     print(file.readline())
#     print(file,'inside')
# print(file,'outside')


"""
file.tell -> возвращает индекс гденаходится курсор(каретка)
file.seek(index)->перемещает курсор на индекс который вы передали
"""

# with open('text.txt', 'r') as file:
# print(file.readline().replace('\n', ''))
# print(file.tell())
# file.seek(0)
# print(file.readline().replace('\n',''))


# data=file.read()
# index=data.index('\n')
# file.seek(index+1)
# print(file.readline().replace('\n',''))


# print(file.readlines()[1].replace('\n',''))
# file.read()
# file.seek(0)
# print(file.readline())

# with open('text.txt','r') as file:
#     print(file.readline(4))
# print(file.readlines(40)) """нашел сороковой символ в файле,а затем вывел все строки которые были до"""

"""изменили модуль с  'r' на 'w'. При запуске, 'w' сразу удаляет все содержимое файла.Если изменить на 'a' тоновая инфа просто
# втсавляется не удаляя"""
# with open('text.txt', 'a') as file:
#     file.write('first string\n')
#     file.write('second string\n')
#     file.write('third lesson\n')
#     file.seek(0)
#     data = ['Bilal is genius!', 'Tima is beast boy!']
#     file.writelines(data)


"""используя 'r+' , данные перезаписываются,то есть старные данные удаляются,и пишутся новые.
а 'a+' не удаляя добавляет"""
# with open('text.txt', 'a+') as file:
#     file.write('John Snow')
#     file.seek(0)
#     print(file.read())

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import re

def get_imei_code(image):
    string=pytesseract.image_to_string(image)
    # print(string,type(string))
    list_of_imei=re.findall(r'IMEI\d.\s\d+', string)
    with open('imei_codes.txt','w') as file:
        file.writelines(f'{x}\n' for x in list_of_imei)
image='images/imei.jpg'
get_imei_code(image)