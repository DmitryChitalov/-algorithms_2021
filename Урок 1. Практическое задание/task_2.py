#!/usr/bin/env python3

import random

"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Постарайтесь не использовать ф-ции min() и sort() и другие ф-ции!
Подход должен быть максимально алгоритмическим.
"""

def get_min_value_v1(data: list) -> int:
    '''
    Поиск минимального значеия O(n^2)
    По сути является алгоритмом пузырьковой сортировки с возвратом 1-ого элемента в отсортированном массиве
    '''

    data_copy = data.copy()
    for i in range(len(data_copy)):
        for j in range(len(data_copy)):
            if data_copy[i] < data_copy[j]:
                data_copy[i], data_copy[j] = data_copy[j], data_copy[i]
    return data_copy[0]


def get_min_value_v2(data: list) -> int:
    '''
    Поиск минимального значения O(n)
    '''

    result = None
    for x in data:
        if result == None or x < result:
            result = x
    return result


def main():
    data = [random.randint(0,10000) for _ in range(100)]
    print(f'Input data: {data}')
    print(f'Min value v1: {get_min_value_v1(data)}')
    print(f'Min value v2: {get_min_value_v2(data)}')


if __name__ == '__main__':
    main()
