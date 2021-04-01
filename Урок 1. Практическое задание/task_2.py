"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать где какая сложность.

Примечание:
Построить список можно через списковое включение.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

import time
import random

test_list = random.sample(range(-9000,9000),10000)

def test_time_perform(fnc):
    ''' Декоратор '''
    def wrp(*args,**kwargs):
        time_in = time.perf_counter()
        min = fnc(*args,**kwargs)
        time_out = time.perf_counter()
        print(f"performance {fnc.__name__}: {(time_out - time_in):0.6f}")
        print(f"{fnc.__name__} min: {min_val}")
    return wrp

@test_time_perform
def min_N(lst: list):
    '''Сложность функции min_N: O(N) '''
    min = lst[0]
    for i,v in enumerate(lst): # O(N)
        if i == 0: continue
        if min > v:
            min = v
    return min

@test_time_perform
def min_N2(lst: list):
    '''Сложность функции min_N2: O(N^2)'''
    min = lst[0]
    for i,v in enumerate(lst): # O(N)
        min = v
        for j,k in enumerate(lst): # O(N)
            min = min if min < k else k
    return min

'''
TEST on
Core i5-3210M 2.5GHz, 8GB DDR3, WIN10 x64, python 3.9
'''

print("*"*25)

time_in = time.perf_counter()
min_val = min(test_list) # O(n)
time_out = time.perf_counter()
print(f"built_in python return: {min_val}")
# 0.000005 len(test_lst) = 10
# 0.000007 len(test_lst) = 100
# 0.000038 len(test_lst) = 1000
# 0.000280 len(test_lst) = 10000
print(f"performance built_in: {(time_out - time_in):0.6f}") 
print("*"*25)

min_N(test_list) # O(n)
# 0.000010 len(test_lst) = 10
# 0.000018 len(test_lst) = 100
# 0.0000221 len(test_lst) = 1000
# 0.000908 len(test_lst) = 10000
print("*"*25)

min_N2(test_list) # O(n^2)
# 0.000037 len(test_lst) = 10
# 0.000667 len(test_lst) = 100
# 0.153533 len(test_lst) = 1000
# 10.164156 len(test_lst) = 10000
print("*"*25)

