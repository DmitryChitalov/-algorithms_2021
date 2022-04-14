"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается

И прошу вас обратить внимание, что то, что часто ошибочно называют генераторами списков,
на самом деле к генераторам отношения не имеет. Это называется "списковое включение" - list comprehension.
"""


from timeit import Timer


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = []
    for i in range(0,len(nums), 2):
        new_arr.append(i)
    return new_arr


print(func_1(list(range(323))))
print(func_1(list(range(323))))

# Сократил количество перебираемых елементов в два раза и убрав условный оператор получил время в два раза меньшее

t1 = Timer("func_1(list(range(323)))", "from __main__ import func_1")
print(t1.timeit(number=100000), " >>>t1")
t2 = Timer("func_2(list(range(323)))", "from __main__ import func_2")
print(t2.timeit(number=100000), " >>>t2")
