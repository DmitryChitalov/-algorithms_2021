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
    new_arr = [num for num in range(len(nums)) if nums[num] % 2 == 0]
    return new_arr


nums = [i for i in range(1000)]

print(timeit("func_1(nums)", "from __main__ import func_1, nums", number=1000))     # 0.1125
print(timeit("func_2(nums)", "from __main__ import func_2, nums", number=1000))     # 0.0849
print()
print(timeit("func_1(nums)", "from __main__ import func_1, nums", number=10000))    # 1.1919
print(timeit("func_2(nums)", "from __main__ import func_2, nums", number=10000))    # 0.8784

# Вывод: Преимущество в производительсности у list comprehension (func_2) примерно в 1,5 раза,
# чем цикл с функцией добавления.