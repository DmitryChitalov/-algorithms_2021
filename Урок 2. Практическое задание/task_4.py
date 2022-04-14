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


def series_sum(max_count: int, element: float = 1, count: int = 0) -> float:
    if count >= max_count:
        return 0

    return element + series_sum(max_count, element/(-2), count+1)


while True:
    try:
        user_num = int(input(f'Введите количество элементов: '))
    except ValueError:
        continue
    print(f'Количество элементов: {user_num}, их сумма: {series_sum(user_num)}')
    break
