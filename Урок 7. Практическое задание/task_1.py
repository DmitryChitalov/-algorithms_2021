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

def sort_bubble(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj

def sort_bubble_1(lst_obj):
    n = 1
    orig_list = lst_obj[:]
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        if orig_list == lst_obj:
            break
        else:
            n += 1
    return lst_obj



origin_list = [random.randint(-100, 100) for _ in range(100)]
sort_list = sort_bubble(origin_list[:])
print(origin_list)
print(sort_list)


# замеры 100
print(
    timeit.timeit(
        "sort_bubble(origin_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "sort_bubble_1(origin_list[:])",
        globals=globals(),
        number=1000))

"""
Вывод:

Сортировка пузырком - 0.619256875
Сортировка пузырком с проверкой - 0.67282875

В связи с низкой вероятностью "1 к len(lst_obj)" сортировка "пузырком" 
только усложняется дополнительной проверкой на предмет изначально отсортированного массива.

"""