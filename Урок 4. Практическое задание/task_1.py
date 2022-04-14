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
from timeit import  timeit

def func_1(nums):
    """Method 1 """
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    """Method 2 """
    return [i for i in nums if not nums[i] % 2]

def func_3(nums):
    """Method 3 """
    return list(i for i in nums if not nums[i] % 2)

print(timeit('func_1(list(range(1000000)))',globals=globals(),number=10))
print(timeit('func_2(list(range(1000000)))',globals=globals(),number=10))
print(timeit('func_3(list(range(1000000)))',globals=globals(),number=10))
l1 = func_1(range(1000))
l2 = func_2(range(1000))
l3 = func_3(range(1000))
print(l1 == l2 == l3)
"""
1.4254638
1.0524819
1.2244305999999998
True
Для ускорения работы использовал LC и всроенную операцию list.
Ускорение составило 40% и 20%, но странно, что list работает медленнее LC
"""
