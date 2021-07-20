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
from timeit import default_timer


def create_lst(nums):
    """Make data"""
    return [random.randint(-100, 99) for i in range(nums)]


def bubble_sort(in_array):
    """Simple sort"""
    start = default_timer()
    work_array = in_array.copy()
    for i in range(len(work_array) - 1):
        for j in range(len(work_array) - 1 - i):
            if work_array[j] < work_array[j + 1]:
                work_array[j], work_array[j + 1] = work_array[j + 1], work_array[j]
    print(f'Working time buble sort:{default_timer() - start}')
    return work_array


def mod_bubble_sort(in_array):
    """Mod sort"""
    start = default_timer()
    work_array = in_array.copy()
    exchange_flag = True
    for i in range(len(work_array) - 1):
        if not exchange_flag:
            break
        for j in range(len(work_array) - 1 - i):
            exchange_flag = False
            if work_array[j] < work_array[j + 1]:
                exchange_flag = True
                work_array[j], work_array[j + 1] = work_array[j + 1], work_array[j]
    print(f'Working time mod buble sort:{default_timer() - start}')
    return work_array


lst = create_lst(50000)
print(lst)
print(bubble_sort(lst))
print(mod_bubble_sort(lst))

"""
Working time buble sort:223.31953
Working time mod buble sort:69.4382048
По результатам видно, что с ростом количества членов массива модифицированная сортировка показывает лучшие
результаты, но это связано с тем,что елементы массива, из-за небольшого их диапазона, начинают повторятся.
На большом массиве уникальных элементов выигрыша не будет.
"""
