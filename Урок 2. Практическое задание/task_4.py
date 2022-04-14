"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Массив в этом задании строить нельзя!
Нужно решить без него!

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_1(n):
    def sum_2(el, num=1):
        if el <= 0:
            return 0
        else:
            return num + sum_2(el - 1, -num / 2)

    print(f'Сумма элементов: {sum_2(n)}')


sum_1(int(input('Введите количество суммируемых элементов: ')))
