from random import randint
from timeit import timeit
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


def bubble_sort_1(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_2(lst_obj):
    """
    для смены направления сортировки поменяли знак на "<", добавили else и получили сокарщение по
    времени работы скрипта более чем в два раза в некоторых случаях.
    Доработка поможет случае если созданный массив будет сразу отсортирован, с увеличением массива
    данная доработка лишается смысла.
    :param lst_obj:
    :return:
    """
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
            else:
                break
        n += 1
    return lst_obj


orig_list = [randint(-100, 100) for _ in range(10)]
print(orig_list[:])
print(bubble_sort_1(orig_list[:]))
print(bubble_sort_2(orig_list[:]))

print(timeit("bubble_sort_1(orig_list[:])", globals=globals(), number=1000))  # 0.01732245499442797
print(timeit("bubble_sort_2(orig_list[:])", globals=globals(), number=1000))  # 0.006569757999386638
