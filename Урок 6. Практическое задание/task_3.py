"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
from memory_profiler import profile

"""Чтобы профилировать функцию-рекурсию, обернем ее декоратором и будем профилировать уже декоратор"""

@profile
def fun_dec(func):
    def wrapper(*argv):
        return func(*argv)
    return wrapper

"""Функция делает реверс строки"""
@fun_dec
def get_numb_reverse(numb, rev_numb=''):
    if numb == 0:
        return rev_numb
    else:
        last_numb = numb % 10
        rev_numb += str(last_numb)
        return get_numb_reverse(numb // 10, rev_numb)


print(get_numb_reverse(12345678901234567890))