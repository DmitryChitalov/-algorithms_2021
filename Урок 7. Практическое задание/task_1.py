"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

from timeit import timeit
from random import randint


def sort_array(array):
    """
    Классическая функция сортировки пузырьком.
    """
    for _ in range(len(array)):
        for element in range(len(array) - 1):
            if array[element] < array[element + 1]:
                array[element + 1], array[element] = array[element], array[element + 1]
    return array


def sort_array_upgrade(array):
    """
    Доработанная функция сортировки с использованием флага и уменьшения колличества иттераций.
    """
    len_list = len(array)
    while len_list > 1:
        flag = True
        for element in range(len_list - 1):
            if array[element] < array[element + 1]:
                array[element], array[element + 1] = array[element + 1], array[element]
                flag = False
        if flag:
            return array
        len_list -= 1
    return array


random_array_10 = [randint(-100, 100) for _ in range(10)]
random_array_100 = [randint(-100, 100) for _ in range(100)]
random_array_1000 = [randint(-100, 100) for _ in range(1000)]

print(random_array_10)
print(sort_array(random_array_10.copy()))
print(sort_array_upgrade(random_array_10.copy()))

print(f'Стандартная сортировка список 10: '
      f'{timeit("sort_array(random_array_10.copy())", globals=globals(), number=1000)}')
print(f'Доработанная сортировка список 10: '
      f'{timeit("sort_array_upgrade(random_array_10.copy())", globals=globals(), number=1000)}')

print(f'Стандартная сортировка список 100: '
      f'{timeit("sort_array(random_array_100.copy())", globals=globals(), number=1000)}')
print(f'Доработанная сортировка список 100: '
      f'{timeit("sort_array_upgrade(random_array_100.copy())", globals=globals(), number=1000)}')

print(f'Стандартная сортировка список 1000: '
      f'{timeit("sort_array(random_array_1000.copy())", globals=globals(), number=1000)}')
print(f'Доработанная сортировка список 1000: '
      f'{timeit("sort_array_upgrade(random_array_1000.copy())", globals=globals(), number=1000)}')


'''
[-49, 68, 5, -83, 19, 13, -97, -86, -25, 25]
[68, 25, 19, 13, 5, -25, -49, -83, -86, -97]
[68, 25, 19, 13, 5, -25, -49, -83, -86, -97]
Стандартная сортировка список 10 элементов 0.011587399999999998
Доработанная сортировка список 10 элементов 0.010045100000000001

Стандартная сортировка список 100 элементов 0.882776
Доработанная сортировка список 100 элементов 0.7582925

Стандартная сортировка список 1000 элементов 106.5490396
Доработанная сортировка список 1000 элементов 86.48994909999999

Скорость сортировки повысилась при использование доработанной функции.
Доработка вида возвращать список если не было произведено ни одной операции присваивания -  
не имеет смысла, так как вероятность такого случая крайне мала.
'''
