"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
from random import randint
from timeit import default_timer


def time_mem_decor(func):
    def wrapper(lst):
        time_start = default_timer()
        res = func(lst)
        time_diff = default_timer() - time_start
        print(f'Время  "{func.__name__}": {time_diff}')
        return res

    return wrapper


@time_mem_decor
def bubble_sort_desc(lst_obj, n=1):
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


@time_mem_decor
def bubble_sort_desc_opti(lst_obj, n=1):
    while n < len(lst_obj):
        transpositions = 0
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                transpositions += 1
        if transpositions == 0:
            return lst_obj
        n += 1
    return lst_obj


# [-100; 100) = {-100 <= x < 100}
my_lst = [randint(-100, 99) for _ in range(1000)]

print(bubble_sort_desc(my_lst[:]))
print(bubble_sort_desc_opti(my_lst[:]))

'''
Время  "bubble_sort_desc": 0.21967790599999998
Время  "bubble_sort_desc_opti": 0.24543891999999995

Создана переменная transpositions, обнуляющаяся при старте прохода цикла while.
Инкремент этой переменной происходит при выполнении условия в цикле for.
После выполнения цикла for проверяется число выполнений условий.
Если 0 - сортировка закончена.

Эта доработка не помогла. 
Даже наоборот: время функции, в основном, увеличилось ~ на 10%.
'''