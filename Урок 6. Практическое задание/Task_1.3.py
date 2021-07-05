from decor import decor
from numpy import array

"""
Задачи из Алгоритмов и структур
Задача №1 из 4 урока
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
"""

# Начальная версия
@decor
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# Оптимизированый вариант
@decor
def func_2(nums):
    new_arr = array([i for i in range(len(nums)) if nums[i] % 2 == 0])
    return new_arr


@decor
def func_3(nums):
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            yield i

new_list = list(range(1000000))

func_1(new_list)
func_2(new_list)
my_generator = func_3(new_list)

"""
Время работы функции func_1, составило: 0.27705060 сек.
Выполнение функции func_1, заняло: 19.3671875 Mib.
Время работы функции func_2, составило: 0.41518080 сек.
Выполнение функции func_2, заняло: 1.91015625 Mib.
Время работы функции func_3, составило: 0.00001350 сек.
Выполнение функции func_3, заняло: 0.0 Mib.
Выводы: func_1 начальный вариант.
func_2 - улучшеный вариант с использованием nympy(array) по времени выполнения дольше на 70%, зато объем 
занимаемой памяти в 10 раз меньше.
func_3 - решение через генератор, самое быстрое и памяти практически не занимает.
"""