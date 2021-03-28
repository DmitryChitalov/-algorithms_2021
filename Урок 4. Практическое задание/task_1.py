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

from timeit import Timer
from timeit import timeit
from random import randint

def fill_list(amount):
    my_list = []
    for i in range(amount):
        my_list.append(randint(0, 10000))
    return my_list

def func_1(nums):       # Эталонный вариант
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):       # Попробуем через встроенные lambda и enumerate, чтобы индекс не "тащить" отдельно
                        # вторя map+lambda для очистки получаемого списка кортежей от кортежей
    return list(map(lambda x: x[0], filter(lambda x: x[1] % 2 == 0, enumerate(nums))))

def func_3(nums):       # повторяет func_2, но для очистки встроенное преобразование к dict и обратно в list
    return list(dict(filter(lambda x: x[1] % 2 == 0, enumerate(nums))))

def func_4(nums):       # уберем все "лишнее", оставив встроенную enumerate
    return [i for i,x in enumerate(nums) if not x%2]

def func_5(nums):       # попроубуем какой-то выигрыш от "не вытаскивать" значенеи массива по индексу
    new_arr = []
    for i, x in enumerate(nums):
        if x % 2 == 0:
            new_arr.append(i)
    return new_arr

func_list = ['func_1', 'func_2', 'func_3', 'func_4', 'func_5', 'func_1']
my_list = [0, 5, 3, 7, 8, 4]
print('Проверим, что все функции "верно" выбирают список индексов из списка: ', my_list)
f = globals()
for el in func_list:        # Убедимся, что все функции верно выбирают индексы элементов с четным значением
    print(f'Функция {el}: {f[el](my_list)}')

# my_list = range(10000)
my_list = fill_list(10000)
print('Теперь список с размерностью ', len(my_list))
for el in func_list:
    print(f'Функция {el}:', timeit(el+'(my_list)', number=1000, globals=globals()))

#t1 = Timer("func_1(my_list)", setup="my_list=fill_list(10000)", globals=globals())

'''
Результат:

Функция func_1: 1.753318042
Функция func_2: 3.7037612830000004
Функция func_3: 3.546011859
Функция func_4: 1.394236509999999
Функция func_5: 1.811383407000001
Функция func_1: 1.6717626939999999 
(для проверки, завершим с первоначальным вариантом) 
'''

'''
Вывод:
    пробовал, как на шаблонных списках range(1000...), так и на randint() - результаты идентичные
    ранее, считал, что использование встроенных lambda, filter, zip сокращают время - нет, только "красоту"
    Самый эффективный алгоритм (№4), одновременно оказался и самым "простым" с т.з. внешней записи
    (нет этих множественных вложенностей, преобразований и т.д.)
'''