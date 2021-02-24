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

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# выполним замеры
timer_1a = timeit('func_1', setup='from __main__ import func_1', number=1000)
print('test_1a meter append even list', timer_1a, 'msec')
timer_2a = timeit('func_1', setup='from __main__ import func_1', number=100000)
print('test_2a meter append even list', timer_2a, 'msec')
timer_3a = timeit('func_1', setup='from __main__ import func_1', number=1000000)
print('test_3a meter append even list', timer_3a, 'msec')
print()


# добавим оптимизацию в код

def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


# выполним замеры автоматизированного кода
timer_1b = timeit('func_2', setup='from __main__ import func_2', number=1000)
print('test_1b append even list', timer_1b, 'msec')
timer_2b = timeit('func_2', setup='from __main__ import func_2', number=100000)
print('test_2b append even list', timer_2b, 'msec')
timer_3b = timeit('func_2', setup='from __main__ import func_2', number=1000000)
print('test_2b append even list', timer_3b, 'msec')

'''
Результаты тестов на моём пк:
test_1a append even list 4.953999996359926e-05 msec
test_2a append even list 0.004443503999937093 msec
test_3a append even list 0.025968484000259195 msec

test_1b append even list 1.377099943056237e-05 msec
test_2b append even list 0.0014098659994488116 msec
test_2b append even list 0.012610267000127351 msec

Как мы видим что есть заметная разница между временем выполнения. Я переделал
функцию для создания списка через списковое включение, потому что оно работает
быстрее итератора с функцией append. Тесты показали наглядно что это действительно
так, а значит код был оптимизирован успешно.
'''
