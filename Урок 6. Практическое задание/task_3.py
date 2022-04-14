"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

from memory_profiler import profile


@profile
def reverse_num(numb):
    def revers_number(num):
        if num == 0:
            return ''
        else:
            return str(num % 10) + revers_number(num // 10)

    return revers_number(numb)


reverse_num(420420)
# Насчет подводных камней, я смог избежать профилирования каждого вызова рекурсии путем
# 'заворачивания' рекурсии в еще одну функцию
