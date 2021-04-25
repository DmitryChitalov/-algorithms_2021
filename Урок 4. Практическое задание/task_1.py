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


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if i % 2 == 0]
    return new_arr


n = [el for el in range(10000)]

print('func_1() - метод append в цикле for:')
print(timeit('func_1(n)', globals=globals(), number=1000))
print('func_2() - списковое включение/list comprehesion:')
print(timeit('func_2(n)', globals=globals(), number=1000))

'''
#Так тоже работает (было актуально до версии 3.5 включительно):
if __name__ == '__main__':
    import timeit
    print(timeit.timeit('func_1(n)', setup ='from __main__ import func_1, n', number=1000))
    print(timeit.timeit('func_2(n)', setup ='from __main__ import func_2, n', number=1000))
'''

'''
func_1() - метод append в цикле for:
2.4427254000000005
func_2() - списковое включение/list comprehension:
1.4229707999999999
Сложность обеих функций О(n) - линейная, однако списковое включение работает несколько быстрее, 
т.к. не используется метод append
'''
