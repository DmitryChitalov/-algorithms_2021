"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
from random import randint
from timeit import timeit


def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        n += 1
    return array


def min_bubble_sort(array):
    for n in range(1, len(array)):
        is_sorted = True
        for i in range(len(array) - n):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                is_sorted = False
        if is_sorted:
            break
    return array


test_list = [randint(-100, 100) for _ in range(10)]
print(f'Исходный массив: {test_list}')
print(f'Массив, отсортированный методом пузырька:\n{bubble_sort(test_list[:])}')
print(f'Массив, отсортированный оптимизированным методом пузырька:\n{min_bubble_sort(test_list[:])}')

print()
test_list = [randint(-100, 100) for _ in range(10)]
print('Замеры дял n=10')
print(timeit("bubble_sort(test_list[:])", globals=globals(), number=1000))
print(timeit("min_bubble_sort(test_list[:])", globals=globals(), number=1000))
print()

test_list = [randint(-100, 100) for _ in range(100)]
print('Замеры дял n=100')
print(timeit("bubble_sort(test_list[:])", globals=globals(), number=1000))
print(timeit("min_bubble_sort(test_list[:])", globals=globals(), number=1000))
print()

test_list = [randint(-100, 100) for _ in range(1000)]
print('Замеры дял n=1000')
print(timeit("bubble_sort(test_list[:])", globals=globals(), number=1000))
print(timeit("min_bubble_sort(test_list[:])", globals=globals(), number=1000))
print()

test_list = list(range(1000))
test_list.reverse()
print('Лучший случай, отсортированный массив n=1000')
print(timeit("bubble_sort(test_list[:])", globals=globals(), number=1000))
print(timeit("min_bubble_sort(test_list[:])", globals=globals(), number=1000))
print()

test_list = list(range(1000))
print('Худший случай, обратный порядок элементов n=1000')
print(timeit("bubble_sort(test_list[:])", globals=globals(), number=1000))
print(timeit("min_bubble_sort(test_list[:])", globals=globals(), number=1000))

"""
Оптимизации:
Заменён внешний цикл while на for.
Добавлен флаг досрочного выхода из цикла,
если не произведено ни одной сортировки.

Для маленьких значений n, есть незначительное улучшение по времени.
С ростом количества элементов в массиве дополнительные проверки
замедляют производительность и время работы ухудшается.
За исключением лучшего случая и досрочного выхода из функции сортировки.

Результат: существенного улучшения данная доработка не дала.

Замеры дял n=10
0.013512799999999998
0.011763099999999999

Замеры дял n=100
0.9088528
0.8510979999999999

Замеры дял n=1000
88.7471766
93.5891389

Лучший случай, отсортированный массив n=1000
32.55852170000003
0.07061019999997598

Худший случай, обратный порядок элементов n=1000
132.9107221
142.9454568
"""
