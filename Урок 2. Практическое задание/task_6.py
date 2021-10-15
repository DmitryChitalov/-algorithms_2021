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

from random import randint as ran


def func(num_x, attempts=10):
    if not attempts:
        print('Конец игры!')
        return
    try:
        x = int(input('Введите число от 0 до 100 '))
    except ValueError:
        print('Введите число!')
        func(num_x, attempts)
        return
    if x == num_x:
        print('Вы угадали число!')
        return
    if x > num_x:
        print('Ваше число больше')
    else:
        print('Ваше число меньше')
    attempts -= 1
    print(f'Осталось попыток {attempts}')
    func(num_x, attempts)


if __name__ == '__main__':
    num = ran(0, 100)
    func(num)

