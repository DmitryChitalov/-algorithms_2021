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

some_list = [randint(-100, 100) for _ in range(0, 100)]


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_improved(lst_obj):
    n = 1
    while n < len(lst_obj):
        check_obj = lst_obj.copy()  # Создание списка с которым будем сравнивать массив после прохода
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        if check_obj == lst_obj:
            break  # Выход из цикла если данный массив уже отсорирован
        n += 1
    return lst_obj


print(timeit('bubble_sort(some_list[:])', globals=globals(), number=10000))  # 11.417191205
print(timeit('bubble_sort_improved(some_list[:])', globals=globals(), number=10000))  # 11.78306

# Смысла в данном улучшении нет, так как цикл прерывается только когда массив уже полностью отсорирован
# вероятность этого близка к нулю
