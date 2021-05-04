"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""


from timeit import timeit
from random import randint


# исходный вариант
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


#  вариант c использованием цикла и enumerate
def func_2(nums):
    new_arr = []
    for i, x in enumerate(nums):
        if x % 2 == 0:
            new_arr.append(i)
    return new_arr


#  вариант c использованием генератора и range
def func_3(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


#  вариант c использованием генератора и enumerate
def func_4(nums):
    return [i for i, x in enumerate(nums) if x % 2 == 0]


nums_list = [randint(0, 100) for i in range(0, 1000)]

print(timeit("func_1(nums)", globals=globals(), number=10000))    # 0.924146  sec.
print(timeit("func_2(nums)", globals=globals(), number=10000))    # 0.9396347 sec.
print(timeit("func_3(nums)", globals=globals(), number=10000))    # 0.6973547 sec.
print(timeit("func_4(nums)", globals=globals(), number=10000))    # 0.7249691 sec.
"""
Самый быстрый - вариант 3 - генератор списка с использованием  range.
                вариант 4 - генератор списка с использованием  enumerate выигрывает в скорости
                            у варианта 3 в случае уменьшения входного списка.
                вариант 2 - аналогично с вариантом 4 по отношению к варианту 1
Генератор позволяет нам формировать новый список сразу при последовательном чтении элементов входящего списка без 
использования промежуточных присваиваний и/или дополнительных обращений к входящему списку.
"""
