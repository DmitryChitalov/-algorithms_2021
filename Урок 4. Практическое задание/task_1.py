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

from timeit import timeit, repeat, default_timer

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

# решение с использованием list comprehension, через вычисление индексов, без присвоение переменной
def func_2(nums):
    # new_arr = [nums.index(num) for num in nums if num % 2 == 0]
    return [nums.index(num) for num in nums if num % 2 == 0]

# решение с использованием list comprehension, через обращение к индексам через len(),
# без присвоение переменной
def func_3(nums):
    # new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]

# решение с аналогичное первому, через цикл for, но с вычислением индексов подходящих
# по условию элементов, через обращение к индексам через len(), с созданием пустого списка и заполнением
def func_4(nums):
    new_arr = []
    for num in nums:
        if num % 2 == 0:
            new_arr.append(nums.index(num))
    return new_arr


num_list = [4, 99, 2, 6, 11, 444, 1000, 77]

print(func_1(num_list))
print(func_2(num_list))
print(func_3(num_list))
print(func_4(num_list))


print(timeit("func_1(num_list)", setup="from __main__ import func_1, num_list", number=1000000))
print(timeit("func_2(num_list)", setup="from __main__ import func_2, num_list", number=1000000))
print(timeit("func_3(num_list)", setup="from __main__ import func_3, num_list", number=1000000))
print(timeit("func_4(num_list)", setup="from __main__ import func_4, num_list", number=1000000))
print()
#
print('Минимальное время выполнения 1000000 вызовов  среди 6 замеров по каждой функции:')
print(min(repeat("func_1(num_list)", "from __main__ import func_1, num_list", default_timer, 6, 1000000)))
print(min(repeat("func_2(num_list)", "from __main__ import func_2, num_list", default_timer, 6, 1000000)))
print(min(repeat("func_3(num_list)", "from __main__ import func_3, num_list", default_timer, 6, 1000000)))
print(min(repeat("func_4(num_list)", "from __main__ import func_4, num_list", default_timer, 6, 1000000)))

# 2.2135099 время выполнения 1000000 вызовов func_1
# 2.3866480999999995  время выполнения 1000000 вызовов func_2
# 2.0774792999999994 время выполнения 1000000 вызовов func_3
# 2.319655  время выполнения 1000000 вызовов func_4

# 2.1222987999999994 минимальное  время выполнения 1000000 вызовов func_1  среди 6 замеров
# 2.3246064000000004  минимальное  время выполнения 1000000 вызовов func_2  среди 6 замеров
# 2.1031751999999955  минимальное  время выполнения 1000000 вызовов func_3  среди 6 замеров
# 2.2536665000000013   минимальное  время выполнения 1000000 вызовов func_4  среди 6 замеров

# вывод: оптимизировть func_1 с небольшим отрывом мне удалось только в func_3 -
# с использованием list comprehension, через обращение к индексам через len(),без присвоение переменной.
# Сложность метода index списков O(n), в сочетании со сложностью цикла дает уже квадратичную сложность, поэтому
# func_2, func_4 - самые затраные по времени.
# list comprehension  через обращение к индексам через len() очень лаконичен, имеет сложность O(N),
# отказ от использования переменной для хранения полученного списка (что и не нужно в данном случае).

# так как временной отрыв func_3 от func_1 в меньшую сторону выглядел спорным (+/-), рассчитала
# минимальное время выполнения 1000000 вызовов  среди 6 замеров по каждой функции.
# результат подтверждает меньшее (хоть и незначительно) время выполнения func_3:

# 2.1222987999999994 минимальное  время выполнения 1000000 вызовов func_1  среди 6 замеров
# 2.3246064000000004  минимальное  время выполнения 1000000 вызовов func_2  среди 6 замеров
# 2.1031751999999955  минимальное  время выполнения 1000000 вызовов func_3  среди 6 замеров
# 2.2536665000000013   минимальное  время выполнения 1000000 вызовов func_4  среди 6 замеров

