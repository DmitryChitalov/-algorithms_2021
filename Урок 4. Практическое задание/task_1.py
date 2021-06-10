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
import timeit as tt



def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


num = [el for el in range(2000)]

t1 = tt.timeit("func_1(num)", globals=globals(), number = 1000)
print(f'Время замера составило: {t1}')

def func_2(nums):
    new_arr = filter(lambda i: nums[i] % 2 == 0, range(len(nums)))
    return new_arr

t2 = tt.timeit("func_2(num)", globals=globals(), number= 1000)
print(f'Время замера составило: {t2}')


#Замер 1 - 0.1199333
#Замер 2 - 0.000422
#Вывод: встроенная функция filter и лямбда-функция работает значительно быстрее чем решение с примененением цикла for
