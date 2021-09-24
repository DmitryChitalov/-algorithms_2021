"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Подсказка:
Базовый случай здесь - угадали число или закончились попытки
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
import  random

def is_netural_number(parametr_x):
    try:
        parametr_x = int(parametr_x)
        if parametr_x < 1 or parametr_x > 100:
            raise TypeError
    except TypeError:
        parametr_x = is_netural_number(input('Вы ввели число не соответствующее диапазону'))
    except ValueError:
        parametr_x = is_netural_number(input('Вы ввели не цело число, введите, пожалуйста, число: '))
    return parametr_x

number = random.randint(1, 100)


def guess_number(number, summ_attempt = 10):
    number_user = is_netural_number(input('Введите число '))
    if number_user == number:
        print('Поздравляю вы угадали')
        return
    else:
        summ_attempt -=1
        if summ_attempt == 0:
            print('У вас закончились попытки')
            return
    if number < number_user:
        print('Вы ввели число больше загаданого \nосталось попыток - ', summ_attempt)
        guess_number(number, summ_attempt)
    else:
        print('Вы ввели число меньше загаданого \nосталось попыток - ', summ_attempt)
        guess_number(number,summ_attempt)

guess_number(random.randint(1, 100))