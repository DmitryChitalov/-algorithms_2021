"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак
"""


def check_val():
    try:
        elements = input('Введите количество элементов: ')
        if not elements.isdigit():
            raise ValueError('Введено не число!')
    except ValueError as err:
        print(err)
    else:
        return get_series_sum(int(elements))


def get_series_sum(elements, result=0, item=1):
    if not elements:
        return result
    result += item
    item = item/(-2)
    elements -= 1
    return get_series_sum(elements, result, item)


print(check_val())

