"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""


from timeit import timeit


data_list = [i for i in range(1000)]


#print(f'Стандартный цикл: {timeit("basic_func()", globals=globals())}')
#print(f'Стандартный цикл: {timeit("optimized_func()", globals=globals())}')
