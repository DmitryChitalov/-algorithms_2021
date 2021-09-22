#!/usr/bin/env python3

import random

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

secret_value = random.randint(0, 101)


def process(counter: int) -> None:
    if counter:
        while True:
            try:
                value = int(input('Введите число от 0 до 100: '))
                if value > 100:
                    raise ValueError()
            except ValueError:
                print ('Неверное число!')
            else: break

        if value < secret_value:
            print (f'Ваше число меньше, осталось {counter - 1} попыток')
            process(counter - 1)
        elif value > secret_value:
            print (f'Ваше число больше, осталось {counter - 1} попыток')
            process(counter - 1)
        else:
            print('Вы угадали! ')
    else:
        print(f'Загаданное число {secret_value}')



def main():
    process(10)


if __name__ == '__main__':
    main()
