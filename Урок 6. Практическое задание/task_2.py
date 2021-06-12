"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""
from task_1_1 import memory_time_profiler


@memory_time_profiler
def list_full(n):
    ls = []
    for i in range(n):
        ls.append(i)
    return ls


@memory_time_profiler
def l_comprehension(n):
    return [i for i in range(n)]


if __name__ == '__main__':
    list_full(100)
    l_comprehension(100)

"""
Цикл
Время выполнения: 0.2304181
Используемая память: 0.00390625 MiB

List comprehension
Время выполнения: 0.22485390000000005
Используемая память: 0.0 MiB
List comprehension выигрывает по отношению к комбинации цикла for + append не только в скорости, но и используемой 
памяти. Однако списковое включение будет все равно уступать map, так что именно последний вариант необходимо
использовать, когда это возможно.
"""
