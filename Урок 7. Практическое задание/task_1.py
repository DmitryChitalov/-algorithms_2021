"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и укажите дала ли оптимизация эффективность.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

import random
import timeit


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


orig_list_1 = [random.randint(-100, 100) for _ in range(10)]
print(orig_list_1)
print(bubble_sort(orig_list_1[:]))

print(
    f'Время выполнения bubble_sort при 10 элементах массива: '
    f'{timeit.timeit("bubble_sort(orig_list_1[:])", globals=globals(), number=1000)}')

orig_list_2 = [random.randint(-100, 100) for _ in range(100)]

print(
    f'Время выполнения bubble_sort при 100 элементах массива: '
    f'{timeit.timeit("bubble_sort(orig_list_2[:])", globals=globals(), number=1000)}')

orig_list_3 = [random.randint(-100, 100) for _ in range(1000)]

print(
    f'Время выполнения bubble_sort при 1000 элементах массива: '
    f'{timeit.timeit("bubble_sort(orig_list_3[:])", globals=globals(), number=1000)}')


# вариант с доработкой
def bubble_sort_revision(lst_obj):
    n = 1
    while n < len(lst_obj):
        flag = False
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag = True
        if not flag:
            break
        n += 1
    return lst_obj


orig_lst_1 = [random.randint(-100, 100) for _ in range(10)]
print(orig_lst_1)
print(bubble_sort_revision(orig_lst_1[:]))

print(f'Время выполнения bubble_sort_revision при 10 элементах массива: '
      f'{timeit.timeit("bubble_sort_revision(orig_lst_1[:])", globals=globals(), number=1000)}')

orig_lst_2 = [random.randint(-100, 100) for _ in range(100)]

print(f'Время выполнения bubble_sort_revision при 100 элементах массива: '
      f'{timeit.timeit("bubble_sort_revision(orig_lst_2[:])", globals=globals(), number=1000)}')

orig_lst_3 = [random.randint(-100, 100) for _ in range(1000)]

print(f'Время выполнения bubble_sort_revision при 1000 элементах массива: '
      f'{timeit.timeit("bubble_sort_revision(orig_lst_3[:])", globals=globals(), number=1000)}')

'''
Время выполнения bubble_sort при 10 элементах массива: 0.017713124000000004
Время выполнения bubble_sort при 100 элементах массива: 0.696003905
Время выполнения bubble_sort при 1000 элементах массива: 82.375299862
Время выполнения bubble_sort_revision при 10 элементах массива: 0.006906970999992268
Время выполнения bubble_sort_revision при 100 элементах массива: 0.7314297839999995
Время выполнения bubble_sort_revision при 1000 элементах массива: 86.142163812
Выводы:
в оптимизированном варианте был добавлен флаг, благодаря которому можно уменьшить количество проходов по массиву и выйти
из цикла, если все элементы уже отсортированы.
Оптимизация не привела к сильному выигрышу во времени, данная реализация будет полезна разве что при небольшом 
количестве элементов массива.
'''
