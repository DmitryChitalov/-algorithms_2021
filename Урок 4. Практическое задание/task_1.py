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
    new_arr = []
    for i in range(0, len(nums), 2):
        new_arr.append(i)
    return new_arr


def func_3(nums):
    return [i for i in range(0, len(nums), 2)]


# Замеряем
nums = [num ** 2 for num in range(10)]
print(f'10. range_1 {timeit(f"func_1({nums})", globals=globals())}')  # 10. range_1 0.8838091
print(f"10. range опт {timeit(f'func_2({nums})', globals=globals())}")  # 10. range опт 0.47523020000000005
print(f"10. lc {timeit(f'func_3({nums})', globals=globals())}")  # 10. lc 0.4288350999999999
nums = [num ** 2 for num in range(100)]
print(f"100. range_1 {timeit(f'func_1({nums})', globals=globals())}")  # 100. range_1 6.5456472
print(f"100. range опт  {timeit(f'func_2({nums})', globals=globals())}")  # 100. range опт  2.534587700000001
print(f"100. lc {timeit(f'func_3({nums})', globals=globals())}")  # 100. lc 1.364778900000001
nums = [num ** 2 for num in range(300)]
print(f"300. range_1 {timeit(f'func_1({nums})', globals=globals())}")  # 300. range_1 19.837014099999998
print(f"300. range опт  {timeit(f'func_2({nums})', globals=globals())}")  # 300. range опт  7.545908400000002
print(f"300. lc {timeit(f'func_3({nums})', globals=globals())}")  # 300. lc 4.103578999999996

# В первой функции оптимизировал использование встроенной функции range.
# Зная, что понадобятся только четные элементы, задаем шаг, используя все возможности range.
# Вторая функция - оптимизация - использование List Comprehension с уже оптимизированным range.
# Результаты:
# На малом списке только функция range выдала скорость почти в два раза выше,
# а в сочетании с list Comprehension стала и того выше
# При увеличении количества элементов показатели стали еще лучше: в 2,5 и почти 5 раз
# Надо сказать, что сначала при использовании только LC, увеличение скорости произошло в 1,4 раза на большом списке,
# и уменьшение скорости на малом
# Но после оптимизации range скорость скаканула.
# Встроенные функции - самые оптимальные.
