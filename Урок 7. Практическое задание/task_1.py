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

import timeit
import random


# Исходный код пузырьковой сортировки
def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
print(f'Исходный список: {orig_list}')
print(f'Отсортированный список: {bubble_sort(orig_list)}')


#  Код пузырьковой обратной сортировки с улучшениями
def bubble_sort2(lst_obj):
    n = 1
    while n < len(lst_obj):
        count = 0
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                count += 1
        if count == 0:
            break
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
print(f'Исходный список: {orig_list}')
print(f'Отсортированный список: {bubble_sort2(orig_list)}')

# замеры 10
orig_list = [random.randint(-100, 100) for _ in range(10)]
print('Исходный 10',
      timeit.timeit(
          "bubble_sort(orig_list[:])",
          globals=globals(),
          number=1000))

# замеры 100
orig_list = [random.randint(-100, 100) for _ in range(100)]
print('Исходный 100',
      timeit.timeit(
          "bubble_sort(orig_list[:])",
          globals=globals(),
          number=1000))

# замеры 300
orig_list = [random.randint(-100, 100) for _ in range(300)]
print('Исходный 300',
      timeit.timeit(
          "bubble_sort(orig_list[:])",
          globals=globals(),
          number=1000))

# замеры 10
orig_list = [random.randint(-100, 100) for _ in range(10)]
print('Улучшенный 10',
      timeit.timeit(
          "bubble_sort2(orig_list[:])",
          globals=globals(),
          number=1000))

# замеры 100
orig_list = [random.randint(-100, 100) for _ in range(100)]
print('Улучшенный 100',
      timeit.timeit(
          "bubble_sort2(orig_list[:])",
          globals=globals(),
          number=1000))

# замеры 300
orig_list = [random.randint(-100, 100) for _ in range(300)]
print('Улучшенный 300',
      timeit.timeit(
          "bubble_sort2(orig_list[:])",
          globals=globals(),
          number=1000))

# Вывод: В коде сделал передвижение элементов в обратном на
# Доработка в виде прекращения цикла, если не было ни одного изменения не имеет смысла,
# так как все равно перебираются все элементы, к тому же вероятность, что рандомно выпадет
# отсортированный список крайне мала.
# По идее если ввести счетчик, который будет уменьшать итерируемую часить списка (исключать уже
# отсортированную сторону, то будет быстрее по скорости.
