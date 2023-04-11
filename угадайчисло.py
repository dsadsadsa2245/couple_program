# import random
#
# score = 1
# user_name = input('Введите ваше имя: ')
# yes_or_no = input(f'{user_name}, хотите сыграть в "угадай число"? y/n')
# yes_or_no = yes_or_no.lower()
# total_plays=0
#
# while yes_or_no == 'y':
#     total_plays+=1
#     random_number = random.randint(1, 1000000)
#     if yes_or_no == 'y' or yes_or_no == 'yes':
#         start = int(input('Введите ваше число от 1 до 1000000: '))
#         while start != random_number:
#             score += 1
#             if start < random_number:
#                 start = int(input("Ваше число меньше заданного числа.Попробуйте еше раз: "))
#             if start > random_number:
#                 start = int(input("Ваше число больше заданного числа.Попробуйте еше раз: "))
#         repeat = input(
#             f"Поздравляю, вы угадали.Заданное число было {random_number}.У вас ушло на это {score} "
#             f"попыток.Хотите еше раз?Вы сограли {total_plays} раз. y/n")
#         if repeat == 'n':
#             print("Жаль")
#             break
#         elif repeat == 'y':
#             print('Игра продолжается')
#         else:
#             print("Недопустимое значение")
# #
# # elif yes_or_no=='n':
# #     print('Вы отказались')
help(len())
