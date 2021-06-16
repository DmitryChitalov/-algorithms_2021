# Задание из основ
# Вводим все слова с маленькой буквы, а программа должна их выводить с большой
from memory_profiler import profile


@profile()
def my_func(lst_txt):
    lst_res = []
    for i in lst_txt:
        lst_res.append(i.capitalize())
    return lst_res


@profile()
def my_func2(lst_txt):
    lst_res = []
    return [i.capitalize() for i in lst_txt]


print(*my_func('test1 test2 test3 test4 test5 test 6'.split()))
print(*my_func2('test1 test2 test3 test4 test5 test 6'.split()))

"""
     4     14.6 MiB     14.6 MiB           1   @profile()
     5                                         def my_func(lst_txt):
     6     14.6 MiB      0.0 MiB           1       lst_res = []
     7     14.6 MiB      0.0 MiB           8       for i in lst_txt:
     8     14.6 MiB      0.0 MiB           7           lst_res.append(i.capitalize())
     9     14.6 MiB      0.0 MiB           1       return lst_res
"""

"""
    12     14.6 MiB     14.6 MiB           1   @profile()
    13                                         def my_func2(lst_txt):
    14     14.6 MiB      0.0 MiB           1       lst_res = []
    15     14.6 MiB      0.0 MiB          10       return [i.capitalize() for i in lst_txt]
"""

'''
Оптимизировали функцию через comprehension
Оптимизация происходит за счет отсутствия метода append
'''
