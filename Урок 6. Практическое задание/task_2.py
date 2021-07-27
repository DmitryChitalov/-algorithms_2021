"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""
from memory_profiler import profile
from pympler import asizeof
import itertools

b = [1, 4, 6, 4, 1]
a = itertools.filterfalse(lambda x: x % 2, b)

new_arr = []
for i in b:
    if i % 2 == 0:
        new_arr.append(i)
print(f'Память list: {asizeof.asizeof(new_arr)}')
print(f'Память itertools : {asizeof.asizeof(a)}')
print(*a)
print(new_arr)

# itertools сборник итераторов (полезен)


