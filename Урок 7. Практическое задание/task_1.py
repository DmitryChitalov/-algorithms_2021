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
from random import randint
from timeit import timeit

original_list = [randint(-100, 100) for _ in range(10)]
print(original_list[:])


def bubble_sort_usual(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
    return lst


def break_bubble_sort(lst):
    n = 1
    while n < len(lst):
        k = 0
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                k += 1
        if k == 0:  # условие if не выполнено, если счетчик не переключится
            break
        n += 1
    return lst


def slice_bubble_sort(lst):
    n = 1
    while n < len(lst):
        k = 0
        for i in range(len(lst[k:]) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                k += 1
        n += 1
    return lst


def bubble_sort_with_count(lst):
    n = 1
    counter = 0
    while n < len(lst):
        for i in range(len(lst) - counter - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
        counter += 1
    return lst


print('bubble_sort_usual', timeit('bubble_sort_usual(original_list[:])', globals=globals(), number=1000))
print('break_bubble_sort', timeit('break_bubble_sort(original_list[:])', globals=globals(), number=1000))
print('slice_bubble_sort', timeit('slice_bubble_sort(original_list[:])', globals=globals(), number=1000))
print('bubble_sort_with_count', timeit('bubble_sort_with_count(original_list[:])', globals=globals(), number=1000))

# Вывод.
# bubble_sort_usual 0.02149899999999999
# break_bubble_sort 0.02888339999999999
# slice_bubble_sort 0.026828699999999983
# bubble_sort_with_count 0.01944689999999999

# Разницы в скорости между представленными вариантами нет. Ускорение дает только вариант со счетчиком итераций.
# Решение со срезом не дает эффекта даже при больших массивах. А решение с разрывом цикла может дать эффект
# только в том случае, если randint сгенерирует отсортированный массив, но вероятность невелика.
