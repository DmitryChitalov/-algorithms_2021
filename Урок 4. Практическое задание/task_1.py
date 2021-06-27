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
    return [nums[i] for i in range(len(nums)) if nums[i] % 2 == 0]


def func_3(nums):
    return [i[1] for i in enumerate(nums) if i[1] % 2 == 0]


my_nums = [i*i for i in range(1000000)]
stmnts = ['func_1(my_nums)', 'func_2(my_nums)', 'func_3(my_nums)']

for st in stmnts:
    print(f'{timeit("st", globals=globals(), number=100000)}')
print(f'\n')
print(f'{timeit("func_1(my_nums)", globals=globals(), number=100)}')
print(f'{timeit("func_2(my_nums)", globals=globals(), number=100)}')
print(f'{timeit("func_3(my_nums)", globals=globals(), number=100)}')
"""
В данном случае очень удобно использоваться списковое ключение.
В рамках цикал это сработало, а enumerate еще сильнее ускроило работу 
0.0021687999999999985
0.0021313000000000026
0.0020120000000000138

Если попробавть замерить скорость не через цикл, то результат следующий:
во первых не понимаю, почему возросло время выполнения чуть ли не на порядки? 
во вторых, применение enumerate ухудшает время. Почему так? 
14.7168798
13.4118401
15.849953900000003
15.849953900000003
"""
