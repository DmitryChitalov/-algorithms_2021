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
import random
from timeit import default_timer, timeit


def time_mem(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        result = func(*args, **kwargs)
        print(f'Время: {default_timer() - start_time}')
        return result

    return wrapper


def sorted_bubble_asc(for_sort):
    for i in range(len(for_sort) - 1):
        for j in range(len(for_sort) - i - 1):
            if for_sort[j] < for_sort[j + 1]:
                for_sort[j], for_sort[j + 1] = for_sort[j + 1], for_sort[j]
    return for_sort


def sorted_bubble_asc_pro(for_sort):
    n = 1
    while n <= len(for_sort):
        step = 0
        for j in range(len(for_sort) - n):
            if for_sort[j] < for_sort[j + 1]:
                for_sort[j], for_sort[j + 1] = for_sort[j + 1], for_sort[j]
                step += 1
        if step == 0:
            break
        n += 1
    return for_sort


orig_list_100 = [random.randint(-100, 100) for _ in range(100)]
print('=' * 50)
print('Сортировка без учета проходов, 100 элементов')
print(timeit('sorted_bubble_asc(orig_list_100[:])', globals=globals(), number=100))
print(timeit('sorted_bubble_asc(orig_list_100[:])', globals=globals(), number=1000))
print(timeit('sorted_bubble_asc(orig_list_100[:])', globals=globals(), number=10000))
print('=' * 50)
print('Сортировка с учетом проходов, 100 элементов')
print(timeit('sorted_bubble_asc_pro(orig_list_100[:])', globals=globals(), number=100))
print(timeit('sorted_bubble_asc_pro(orig_list_100[:])', globals=globals(), number=1000))
print(timeit('sorted_bubble_asc_pro(orig_list_100[:])', globals=globals(), number=10000))
print('~=~' * 25)
"""
Результат
==================================================
Сортировка без учета проходов, 100 элементов
0.0697549
0.5158342
5.7579237999999995
==================================================
Сортировка с учетом проходов, 100 элементов
0.0491104
0.48380129999999966
5.8069326000000006
~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~

Результат данного модернизации, фактически не принесет никакого эффекта, т.к. вероятность того, что
массив будет уже отсортирован очень маленькая.
Вероятность повышается с уменьшением количества элементов для сортировки.
"""
