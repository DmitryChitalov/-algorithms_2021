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
from itertools import filterfalse


# Создание тестового списка
test_list = [i for i in range(10000)]


def func_1(nums):
    """Функция использующая цикл for"""
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    """функция использующая List comprehension"""
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


def func_3(nums):
    """функция использующая itertools filterfalse"""
    new_array = list(filterfalse((lambda x: nums[x] % 2 != 0), range(len(nums))))
    return new_array


def func_4(nums):
    """функция использующая map"""
    new_array = list(map((lambda x: nums[x] % 2 != 0), range(len(nums))))
    return new_array


def func_5(nums):
    """функция использующая enumerate"""
    new_arr = [key for key, val in enumerate(nums) if val % 2 == 0]
    return new_arr


"""
Сравнивая представленные варианты по скорости можно выделить 
варианты со списковым включением и вариант с enumerate
как наиболее быстрые для генерации и фильтрации больших объемов.
Цикл for незначительно проигрывает по времени и наконец map и 
filterfalse отстают засчет того, что их О-нотация 2-3n (боюсь ошибиться 
из- за функций list, map и range).
"""

"""1.2757304"""
print(timeit('func_1(test_list)', globals=globals(), number=1000))

"""0.8109587"""
print(timeit('func_2(test_list)', globals=globals(), number=1000))

"""1.3774445000000002"""
print(timeit('func_3(test_list)', globals=globals(), number=1000))

"""1.5288021"""
print(timeit('func_4(test_list)', globals=globals(), number=1000))

"""0.8811968000000006"""
print(timeit('func_5(test_list)', globals=globals(), number=1000))