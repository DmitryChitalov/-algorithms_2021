"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
from memory_profiler import memory_usage, profile
from timeit import default_timer


def time_mem_decor(func):
    def wrapper(lst):
        time_start = default_timer()
        mem_start = memory_usage()
        res = func(lst)
        time_diff = default_timer() - time_start
        mem_diff = memory_usage()[0] - mem_start[0]
        print(f'Время  "{func.__name__}": {time_diff}')
        print(f'Память "{func.__name__}": {mem_diff}')
        return res

    return wrapper


@time_mem_decor
@profile
def get_sum(lst_obj):
    def get_sum_recursion(lst):
        if len(lst) == 1:
            return lst[0]
        else:
            return lst[0] + get_sum_recursion(lst[1:])


my_lst = [i * i for i in range(100000)]
get_sum(my_lst)

'''
Рекурсия спрятана внутри функции, к которой уже применяются декораторы.
Так декораторы не вызываются при каждом рекурсивном вызове функции.
'''