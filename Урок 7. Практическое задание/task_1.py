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
import timeit
import random

test_list = [random.randint(-100, 100) for i in range(100)]
test_list2 = test_list[:]


def bubble_sort(obj):
    list_copy = obj[:]
    n = 1
    while n < len(obj):
        for i in range(len(obj) - n):
            if obj[i] < obj[i + 1]:
                obj[i], obj[i + 1] = obj[i + 1], obj[i]
        n += 1
    return f'Массив до сортировки {list_copy}, Массив после сортировки: {obj}'


print('Время работы первой функции при 100:\n')
print(timeit.timeit("bubble_sort(test_list[:])",
                    setup="from __main__ import bubble_sort, test_list", number=100))
print('Время работы первой функции при 1000:\n')
print(timeit.timeit("bubble_sort(test_list[:])",
                    setup="from __main__ import bubble_sort, test_list", number=1000))
print('Время работы первой функции при 10000:\n')
print(timeit.timeit("bubble_sort(test_list[:])",
                    setup="from __main__ import bubble_sort, test_list", number=10000))


def bubble_sort_optimize(obj):
    n = 1
    while n < len(obj):
        x = 0
        for i in range(len(obj) - n):
            if obj[i] < obj[i + 1]:
                obj[i], obj[i + 1] = obj[i + 1], obj[i]
                x += 1
        if x == 0:
            break
        n += 1
    return f'Oтсортированный массив: {obj}'


print('\nВремя работы доработанной функции - 100 повторов:\n')
print(timeit.timeit("bubble_sort_optimize(test_list2[:])",
                    setup="from __main__ import bubble_sort_optimize, test_list2", number=100))

print('\nВремя работы доработанной функции - 1000 повторов:\n')
print(timeit.timeit("bubble_sort_optimize(test_list2[:])",
                    setup="from __main__ import bubble_sort_optimize, test_list2", number=1000))

print('\nВремя работы доработанной функции - 10000 повторов:\n')
print(timeit.timeit("bubble_sort_optimize(test_list2[:])",
                    setup="from __main__ import bubble_sort_optimize, test_list2", number=10000))


print(bubble_sort(test_list))
print(bubble_sort_optimize(test_list2))

"""
После оптимизации время выполнения при всех значениях повторов стало немного выше. Смысла в оптимизации нет.
"""