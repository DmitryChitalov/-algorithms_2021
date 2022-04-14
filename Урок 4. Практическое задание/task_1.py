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

# print(timeit("func_1(lst)", globals=globals(), number=10))

# t = Timer(stmt="func_1([228, 212, 3346, 44567, 456,  5])", setup="from __main__ import func_1, [228, 212, 3346, 44567, 456,  5]")
# print(t.timeit(number=100))


from timeit import timeit


lst = [228, 212, 3346, 44567, 456,  5]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):                #Применили list comprehension, но он почему-то работает медленее, чем цикл?
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


def func_3(nums):                      #Применили функцию enumerate(), она работает быстрее, чем функция range()
    new_arr = []
    for i, el in enumerate(nums):
        if el % 2 == 0:
            new_arr.append(i)
    return new_arr


print(
    timeit(
        "func_1(lst)",
        globals=globals()
        ))
print(
    timeit(
        "func_2(lst)",
        globals=globals()
        ))
print(
    timeit(
        "func_3(lst)",
        globals=globals()
        ))