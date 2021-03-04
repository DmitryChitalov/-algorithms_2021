"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile


@profile
def cnt(number):
    def count_recur(num=number, even=0, odd=0):
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
        if num == 0:
            return print(f"evens {even}\nodds {odd}")
        count_recur(num, even, odd)
    return count_recur(number)


cnt(35608909)
"""Если замерять как обычно, то получаем таблицу на каждый вызов функции
Для замера нужно обернуть функцию в другую функцию и замерить результ работы функции 'обёртки'"""
