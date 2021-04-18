"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile


#  Сумма n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
@profile
def f_sum(start_value, no_elements):
    if no_elements == 1:
        return start_value
    return start_value + f_sum(0 - (start_value / 2), no_elements - 1)


print(f_sum(100000000, 200))

"""
При запуске f_sum профилирование памяти происходит для КАЖДОГО вызова функции f_sum.
Это хорошо заметно по столбцу Occurences вывода профайлера (он меняется от 1 до 100)
Поэтому, если мы хотим замерить общее время надо просто сделать функцию-обертку над функцией рекурсии
и профилировать именно ее(см.ниже)
"""


@profile
def f_wrap_sum(start_value, no_elements):
    def f_sum_2(start_value, no_elements):
        if no_elements == 1:
            return start_value
        return start_value + f_sum_2(0 - (start_value / 2), no_elements - 1)

    return f_sum_2(start_value, no_elements)


print(f_wrap_sum(100000000, 200))
