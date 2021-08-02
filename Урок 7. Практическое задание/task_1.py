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


# Сортировка с добавлением остановки не проходит по уже отсортированным спискам, следовательно времени затрачивается меньше

def bubble_sort_flag(lst_obj):
    n = 1
    check = False
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                check = True
        if check == False:
            return lst_obj
        n += 1
    return lst_obj



print(f'Сортировка с остановкой, если список уже отсортирован: ')

orig_list = [random.randint(-100, 100) for _ in range(10)]

print(
    timeit.timeit(
        "bubble_sort_flag(orig_list[:])",
        globals=globals(),
        number=1000), print(f'\n{orig_list}\n{bubble_sort_flag(orig_list)}'))

orig_list = [random.randint(-100, 100) for _ in range(100)]

print(
    timeit.timeit(
        "bubble_sort_flag(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

print(
    timeit.timeit(
        "bubble_sort_flag(orig_list[:])",
        globals=globals(),
        number=1000))



def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


print(f'Обычная сортировка пузырьком')


orig_list = [random.randint(-100, 100) for _ in range(10)]

print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000), print(f'\n{orig_list}\n{bubble_sort(orig_list)}'))

orig_list = [random.randint(-100, 100) for _ in range(100)]

print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range (1000)]

print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))


# Сортируется 1 раз и прогоняет по отсортированным
# Сортировка с остановкой, если список уже отсортирован:
# 0.0007833000000000007
# 0.0084749
# 0.09409679999999998
# Обычная сортировка пузырьком
# 0.003669699999999998
# 0.21960049999999998
# 25.391862200000002
#

# При сортировке неотсортированных массивов доработка не имеет улучшения по скорости исполнения
# Сортировка с остановкой, если список уже отсортирован:
# 0.013034900000000002
# 0.7218253000000001
# 50.7222548
# Обычная сортировка пузырьком
# 0.007379400000004921
# 0.3842490999999981
# 48.542889900000006
#
