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


def range_sum(num: int, cur_num: float = 1.0) -> float:
    if num == 1:
        return cur_num
    else:
        return cur_num + range_sum(num-1, cur_num/(-2))


if __name__ == '__main__':
    print(range_sum(3))
    print(range_sum(10))
    print(range_sum(50))
    print(range_sum(500))
