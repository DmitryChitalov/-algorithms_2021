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


from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


def func_3(nums):
    return [i for i in range(len(nums)) if i % 2 == 0]


nums = [el for el in range(1000)]

print(timeit("func_1(nums)", globals=globals(), number=10000))
print(timeit("func_2(nums)", globals=globals(), number=10000))
print(timeit("func_3(nums)", globals=globals(), number=10000))


nums = [el for el in range(100)]

print(timeit("func_1(nums)", globals=globals(), number=10000))
print(timeit("func_2(nums)", globals=globals(), number=10000))
print(timeit("func_3(nums)", globals=globals(), number=10000))


nums = [el for el in range(10)]

print(timeit("func_1(nums)", globals=globals(), number=10000))
print(timeit("func_2(nums)", globals=globals(), number=10000))
print(timeit("func_3(nums)", globals=globals(), number=10000))

"""
Первый вариант заполнения массива представляет собой цикл, 
во втором варианте использовался enumerate,
а в третьем - list comprehension.
Замер для 1000 элементов:
0.7085953
0.5252359
0.40498860000000003

Замер для 100 элементов:
0.07522010000000001
0.049870499999999984
0.0487813

Замер для 10 элементов:
0.009451499999999998
0.0091199
0.008238799999999998


Цикл тратит на заполнение списков большего времени, чем два других способа.
enumerate и цикл одиноково себя проявляют при малом количестве вводимых данных, 
LC ведет себя быстрее при любом количестве элементов.
"""