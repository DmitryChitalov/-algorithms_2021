"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
from memory_profiler import profile

@profile
def decor(func):
    def wrapper(*argv):
        return func(*argv)
    return wrapper

@decor
def get_rev_number(number, rev_number = ''):                        # 0
    if number == 0:                                                 # 0
        return rev_number                                           # 0
    else:
        last_number = number % 10                                   # 0
        rev_number += str(last_number)                              # 0
        return get_rev_number(number // 10, rev_number)             # 0.2

print(get_rev_number(1234))