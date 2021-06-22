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
    return [x for x in nums if x % 2 == 0]


# ??? <filter object at 0x0000018DCE941940>
def func_3(nums):
    res = filter(lambda x: x % 2 == 0, nums)
    return res


def func_4(nums):
    res = []
    gen = filter(lambda x: x % 2 == 0, nums)
    for i in gen:
        res.append(i)
    return res


nums_list = [x for x in range(100)]
# print(nums_list)
t1 = Timer("func_1(nums_list)", "from __main__ import func_1, nums_list")
print(f'Суммарное время 10000 запусков func_1 {t1.timeit(number=10000) * 1000:.5f} мсек')
print('*' * 6)
t2 = Timer("func_2(nums_list)", "from __main__ import func_2, nums_list")
print(f'Суммарное время 10000 запусков func_2 {t2.timeit(number=10000) * 1000:.5f} мсек')
print('*' * 6)
t3 = Timer("func_3(nums_list)", "from __main__ import func_3, nums_list")
print(f'Суммарное время 10000 запусков func_3 {t3.timeit(number=10000) * 1000:.5f} мсек')
print('*' * 6)
t4 = Timer("func_4(nums_list)", "from __main__ import func_4, nums_list")
print(f'Суммарное время 10000 запусков func_4 {t4.timeit(number=10000) * 1000:.5f} мсек')

'''
в ~ 1,5 раза List comprehension лучше цикла,
а цикл в ~ 1,5 раза лучше filter с циклом,
при числе элементов списка около 100
Вывод:
List comprehension лучший вариант для использования.
???
мне не понятно почему func_3 работает как генератор, поэтому в func_4 использовал цикл для формирования списка.
'''
