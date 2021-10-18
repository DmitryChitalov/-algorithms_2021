"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
from memory_profiler import profile


@profile
def sums(f):
    def proof(n):
        if n == 1:
            return 1
        else:
            return n + proof(n - 1)

    result = proof(f)
    return result


print(sums(100))
'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    10     19.5 MiB     19.5 MiB           1   @profile
    11                                         def cache(f):
    12     19.6 MiB      0.1 MiB         101       def proof(n):
    13     19.6 MiB      0.0 MiB         100           if n == 1:
    14     19.6 MiB      0.0 MiB           1               return 1
    15                                                 else:
    16     19.6 MiB      0.0 MiB          99               return n + proof(n - 1)
    17     19.6 MiB      0.0 MiB           1       result = proof(f)
    18     19.6 MiB      0.0 MiB           1       return result


5050

Process finished with exit code 0
'''

'''
Аналитика:
Профилировать рекурсивные функции можно, только необходимо записать результат вызова функции
в переменную и обернуть в еще в одну функцию, чтоб декоратор profile не вызывался рекурсивно
как показано в примере выше
'''
