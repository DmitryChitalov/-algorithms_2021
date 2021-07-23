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


import timeit

my_nums_1000 = [i for i in range(1000)]
my_nums_10000 = [i for i in range(10000)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.insert(-1, nums[i])
    return new_arr


# Списковые включения
def func_3(nums):
    return [i for i, elem in enumerate(nums) if elem % 2 == 0]


def func_4(nums):
    return list(filter(lambda i: (nums[i] % 2 == 0), nums))


# то же самое, что и func_3, но не через генераторное выражение
# по скорости func_3 отрабатывает быстрее, чем func_5
def func_5(nums):
    new_arr = []
    for n, elem in enumerate(nums):
        if elem % 2 == 0:
            new_arr.append(n)
    return new_arr


print(f'func_1: {timeit.timeit("func_1(my_nums_1000)", globals=globals(), number=1000)}')
print('func_2: ', end='')
print(timeit.timeit(
    "func_2(my_nums_1000)",
    globals=globals(),
    number=1000
))
print("func_3: ", end='')
print(timeit.timeit(
    "func_3(my_nums_1000)",
    globals=globals(),
    number=1000
))
print('func_4: ', end='')
print(timeit.timeit(
    "func_4(my_nums_1000)",
    globals=globals(),
    number=1000
))
print('func_5: ', end='')
print(timeit.timeit(
    "func_5(my_nums_1000)",
    globals=globals(),
    number=1000
))
print('\n')

print(f'func_1: {timeit.timeit("func_1(my_nums_10000)", globals=globals(), number=10000)}')
print('func_2: ', end='')
print(timeit.timeit(
    "func_2(my_nums_10000)",
    globals=globals(),
    number=10000
))
print("func_3: ", end='')
print(timeit.timeit(
    "func_3(my_nums_10000)",
    globals=globals(),
    number=10000
))
print('func_4: ', end='')
print(timeit.timeit(
    "func_4(my_nums_10000)",
    globals=globals(),
    number=10000
))
print('func_5: ', end='')
print(timeit.timeit(
    "func_5(my_nums_10000)",
    globals=globals(),
    number=10000
))

# func_1: 0.055393200000000004
# func_2: 0.06055890000000001
# func_3: 0.04984749999999999
# func_4: 0.08805469999999999
# func_5: 0.054581500000000005
# 
# 
# func_1: 5.2117634
# func_2: 6.136458599999999
# func_3: 4.869016400000001
# func_4: 8.7940246
# func_5: 5.908816100000003


# Оптимизоровать код получилось через списковые включения и встроенную функицю enumerate
# Функция 3 всегда выполняется быстрее функции 1.
# На больших массивах функция 5 выполняется дольше, чем функция 1, но если уменьшить размер массива, то функция 5 быстрее функции 1
