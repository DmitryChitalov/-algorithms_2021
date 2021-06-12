"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

from memory_profiler import profile

"""
@profile
def row_sum(n):
    if n > 1:
        return (-0.5) ** (n - 1) + row_sum(n - 1)
    return n


row_sum(2)
"""


@profile
def profiler(num):
    def row_sum(n):
        if n > 1:
            return (-0.5) ** (n - 1) + row_sum(n - 1)
        return n
    return row_sum(num)


print(profiler(3))

"""
Если профилировать непосредственно рекурсивную функцию, мы получим результат для каждого вызова
функции. Чтобы этого избежать, необходимо "обернуть" рекурсивную функцию в другую функцию
и профилировать уже ее.
"""
