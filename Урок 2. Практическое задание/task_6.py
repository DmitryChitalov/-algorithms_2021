"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Подсказка:
Базовый случай здесь - угадали число или закончились попытки
"""
from random import randint


def random_number(number=None, min_number=0, max_number=100, counter=10):
    if counter == 0:
        print('Вы не угадали, попытки закончились!')
    else:
        try:
            print(f'Угадайте число от {min_number} до {max_number}, осталось попыток: {counter}')
            my_number = int(input(f'Введите челое число: '))
            if number is None:  # первичная генерация случайного числа
                number = randint(0, 100)
            if my_number == number:
                return print('Вы угадали! УРА!!!')
            else:
                if my_number < number:
                    min_number = my_number
                    print('==> Число больше <==')
                else:
                    max_number = my_number
                    print('==> Число меньше <==')
                return random_number(number, min_number, max_number, counter - 1)
        except ValueError:
            print('Ошибка, это не число!')
            return random_number(number, min_number, max_number, counter)


random_number()
