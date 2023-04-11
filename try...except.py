"""Обработка исключений"""
# операторы try..except
# Errors -> связаны с кодом
# SyntaxError
# IndentationError
# TabError
# Исключения exceptions ->  связаны с неправильными данными которые передаются в код
# ZeroDivisionError
# ArithmeticError
# NameError
# IndexError
# KeyError


# try:
#     a = int(input('Enter the number: '))
# except:
#     print('неправильные данные')
# else:
#     print(a * 5)

# try:
#     <body>
# except:
#     <body> сработает если есть ошибка
# else:
#     <body> если не найдено ошибок
# finally:
#     <body> сработает в любом случае


# ls = ['John', 'Snow', 'Trilion']
# try:
#     i = int(input('Vvedite index: '))
#     print(ls[i])
# except ValueError:
#     print('Вводите только числа!')
# except IndexError:
#     print('Вы ввели неправильный индекс')

# _________________________________________________________________________
# отображение ошибки
# Exception as e (error)
# dict = {'1': 'one', '2': 'two', 'name': 'John'}
# try:
#     key = input('Введите ключ: ')
#     print(dict[key])
# except Exception as a:
#     print('Oops', a, 'error')  # or print(f'Oops {a.__class__}error')

# try:
#     num1 = int(input("Enter num1"))
#     num2 = int(input("Enter num2"))
#     result=num1/num2
# except ValueError:
#     print("enter only integers")
# except ZeroDivisionError:
#     print('Can not divide zero')
# else:
#     print(int(result))
# finally:
#     print('The end!')
