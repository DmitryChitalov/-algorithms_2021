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


from random import randint


def num_finder(secret, count=10, start=0, stop=100):
    if count == 0:
        return f'Кончились попытки, было загаданно число - {secret}'
    try:
        answer = int(input(f'Назовите число: '))
    except ValueError:
        print('Необходимо вводить числа!')
    if answer == secret:
        return f'Поздравляем вы угадали! Было загадано число {secret}!'
    else:
        if answer > secret:
            count -= 1
            print(f'Ваше число больше! Осталось {count} попыток.')
            return num_finder(secret, count)
        elif answer < secret:
            count -= 1
            print(f'Ваше число меньше! Осталось {count} попыток.')
            return num_finder(secret, count)


print(f'Загадано число от 0 до 100, у вас есть 10 попыток, чтобы его отгадать!')
print(num_finder(randint(0, 100)))
