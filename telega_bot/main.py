import telebot
from telebot import types
import random

my_token='6211231852:AAGLygJl8s4m2UuTnoLXnKnTW27TMnTkxek'
bot=telebot.TeleBot(my_token)
keyboard=types.ReplyKeyboardMarkup()
btn1=types.KeyboardButton('Играть!')
btn2=types.KeyboardButton('Нет,я пасс!')
keyboard.add(btn1,btn2)

@bot.message_handler(commands=['start','game'])
def start_message(message):
    bot_message=bot.send_message(message.chat.id,'Привет Daniel, начнем игру?',reply_markup=keyboard)
    bot.register_next_step_handler(bot_message,check_answer)
    
def check_answer(message):
    if message.text=='Играть!':
        bot.send_message(message.chat.id,"Ok, тогда вот лови правила игры:\nнужно угадать число ,которое я загадаю в дипазоне 1-10 включительно.У тебя будет три попытки,еслт не угадаешь,я тебя порежу! =)")
        number=random.randint(1,10)
        print(number,'!!!!')
        game(message, 3, number)
    elif message.text=='Нет,я пасс!':
        bot.send_message(message.chat.id,'Ну хорошо,пока.')
    else:
        bot_message=bot.send_message(message.chat.id,'Вы ввели неправильный ответ!!!Введите новый!\nВведите новый:',reply_markup=keyboard)
        bot.register_next_step_handler(bot_message,check_answer)
def game(message, attempts,number):
    message_bot=bot.send_message(message.chat.id,'Выбери число: ')
    bot.register_next_step_handler(message_bot, check_number,attempts-1,number)
def check_number(message,attempts,number):
    if message.text==str(number):
        bot.send_message(message.chat.id,'Вы победили! Нарекаю вас удачливым!')
    elif attempts==0:
        bot.send_message(message.chat.id,'ТЫ проиграл!!!!!!')
    else:
        bot.send_message(message.chat.id,'Нет,ты не угадал число, попробуй еще раз!')
        game(message, attempts, number)
bot.polling()

