"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

import copy
from memory_profiler import profile
from sys import getrefcount


@profile
def function_1():
    """Выделяет доп память, не освобождается"""
    x = list(range(100000))
    y = copy.deepcopy(x)
    return y


@profile
def function_2():
    """Выделяет доп память, освобождается"""
    x = list(range(100000))
    print(getrefcount(x))
    y = copy.deepcopy(x)
    print(getrefcount(y))
    del x
    y = None
    return y


if __name__ == "__main__":
    function_1()
    function_2()