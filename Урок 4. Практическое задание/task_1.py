from timeit import timeit

"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


lst = [1, 2, 3, 4, 5, 6]
print(timeit("func_1(lst)", globals=globals()))
print(func_1(lst))

"""
Выбрал списковое включение, так как оно намного быстрее изначального цикла(прочитал в Лутце и пробовал на примерах)
Но тут он возвращает не индекс, а именно элементы
"""


def func_2(nums):
    new_arr = [x for x in nums if x % 2 == 0]
    return new_arr


print(timeit("func_2(lst)", globals=globals()))
print(func_2(lst))

"""
Так же функция map работает быстрее обычного цикла, поэтому решил использовать ее, но он может замедляться из-за
преобразования в список(мои размышления)
"""


def func_3(nums):
    new_arr = list(map(lambda x: x % 2 == 0, nums))
    return new_arr


print(timeit("func_3(lst)", globals=globals()))
print(func_3(lst))
