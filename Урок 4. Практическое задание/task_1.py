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

nums = [i for i in range(10000)]

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    ''' 
    Выполняется быстрее func_1 за счет меньшей вычислительной сложности
    нет сравнения и взятия остатка от деления
    '''
    new_arr = []
    i=0
    cnt = len(nums)-1
    while(i <= cnt):
        new_arr.append(nums[i])
        i+=2
    return new_arr

def func_3(nums): 
    '''
    Выполняется всех быстрее, нет никакой математики
    Индексы массива это целые числа,
    заполняем массив четными числами на длинну исходного массива
    '''
    cnt = (len(nums))//2 if len(nums)%2==0 else (len(nums))//2 +1
    new_arr = [i*2 for i in range(cnt)]
    return new_arr

##########################################################

#print(f"func_1 res: {func_1(nums)}")
#print(f"func_2 res: {func_2(nums)}")
#print(f"func_3 res: {func_3(nums)}")

print(f"func_1 time: {timeit('func_1(nums)',setup='from __main__ import func_1,nums',number=1000)}")
print(f"func_1 time: {timeit('func_2(nums)',setup='from __main__ import func_2,nums',number=1000)}")
print(f"func_3 time: {timeit('func_3(nums)',setup='from __main__ import func_3,nums',number=1000)}")

