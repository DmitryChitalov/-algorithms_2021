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

lst = [randint(-100, 100) for x in range(100)]
print(lst)


def old_bubble_sort(lst_obj):
    n = 0

    while n < len(lst_obj):
        for i in range(len(lst_obj) - 1):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def new_bubble_sort(lst_obj):
    n = 0

    while n < len(lst_obj):
        end_flag = 1
        for i in range(len(lst_obj) - n - 1):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                end_flag = 0
        if end_flag == 1:
            break
        n += 1
    return lst_obj


print(timeit('old_bubble_sort(lst.copy())', globals=globals(), number=10000))  # 7.779501289
print(timeit('new_bubble_sort(lst.copy())', globals=globals(), number=10000))  # 5.17235508

"""
Прервывание цикла после завершения постановки числа в конец, дало преимущество по скорости работы примерно в полтора раза:
old_bubble_sort: 8.3697173
new_bubble_sort: 5.341894999999999
"""
