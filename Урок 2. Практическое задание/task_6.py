"""
Задание 6.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""
import random


def guess_number(number, try_count=1):
    try:
        user_number = int(input('Введите число от 1 до 100: '))
        if user_number == number:
            print('Вы выйграли')
        elif try_count == 10:
            print(f'Вы проиграли. Было загадано число: {number}')
        elif user_number < 0 or user_number > 100:
            print('Загадано число от 1 до 100')
            guess_number(number, try_count)
        else:
            print('Загаданное число меньше') if user_number > number else print('Загаданное число больше')
            try_count += 1
            guess_number(number, try_count)
    except ValueError:
        print('Ошибка ввода. Вы ввели не целое число.')
        guess_number(number, try_count)


if __name__ == '__main__':
    guess_number(random.randint(1, 100))
