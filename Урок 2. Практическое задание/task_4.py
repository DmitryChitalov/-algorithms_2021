"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Массив в этом задании строить не нужно!
Нужно решить без него!

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def crazy_sum(num):
    if num == 1:
        return 1
    else:
        return crazy_sum(num - 1) + \
               (  1 / (2 ** (num - 1)) if num % 2 else \
                 -1 / (2 ** (num - 1)))


if __name__ == '__main__':
    n = int(input('How many CRAZY iterations you need: '))
    print(f'for {n} iterations crazy_sum is {crazy_sum(n)}')

'''
How many CRAZY iterations you need: 3
for 3 iterations crazy_sum is 0.75
How many CRAZY iterations you need: 4
for 4 iterations crazy_sum is 0.625
'''
