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


def sort_bubble_not_optimize(list_obj):
    n = 1
    while n < len(list_obj) - 1:
        for i in range(len(list_obj) - 1):
            if list_obj[i] < list_obj[i + 1]:
                list_obj[i], list_obj[i + 1] = list_obj[i + 1], list_obj[i]
        n += 1
    return list_obj


def sort_bubble_optimize(list_obj):
    n = 1
    flag = 1
    while flag:
        flag = 0
        for i in range(len(list_obj) - n):
            if list_obj[i] < list_obj[i + 1]:
                flag = 1
                list_obj[i], list_obj[i + 1] = list_obj[i + 1], list_obj[i]
        n += 1
    return list_obj


def not_optimize(list_orig):
    return f'Длина списка: {len(list_orig)}\n' \
           f'Список до сортировки: {list_orig}\n' \
           f'Список после сортировки без оптимизации: {sort_bubble_not_optimize(list_orig[:])}\n' \
           f'Замеры времени сортировки до оптимизации: ' \
           f'{timeit.timeit(f"sort_bubble_not_optimize({list_orig[:]})", globals=globals(), number=1000)}\n'


def optimize(list_orig):
    return f'Длина списка: {len(list_orig)}\n' \
           f'Список до сортировки: {list_orig}\n' \
           f'Список после сортировки с оптимизацией: {sort_bubble_optimize(list_orig[:])}\n' \
           f'Замеры времени сортировки после оптимизации: ' \
           f'{timeit.timeit(f"sort_bubble_optimize({list_orig[:]})", globals=globals(), number=1000)}\n'


result_1 = [random.randint(-100, 100) for _ in range(10)]
result_2 = [random.randint(-100, 100) for _ in range(100)]
result_3 = [random.randint(-100, 100) for _ in range(1000)]

# До оптимизации
print(not_optimize(result_1))  # 0.011281229002634063
print(not_optimize(result_2))  # 1.0215907729871105
print(not_optimize(result_3))  # 104.24087570799747

# После оптимизации
print(optimize(result_1))  # 0.006491231004474685
print(optimize(result_2))  # 0.6475550670002121
print(optimize(result_3))  # 65.48425598998438

"""
Оптимизация за счет флага выхода при полностью отсортированном массиве не даёт результатов, так как вероятность того, 
что массив будет сгенерирован отсортированным маловероятна.
Добавлена оптимизация с помощью уменьшения колличества проверяемых элементов массива на единицу после прохождения 
массива, так как после каждого прохождения массива последний элемент всегда будет на своём месте.
В результате оптимизации достигнуто снижение времени.
"""

