"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
from memory_profiler import profile


@profile
def check_memory(n):
    def revers_numbers(number):
        if number == 0:
            return ''
        else:
            return str(number % 10) + revers_numbers(number // 10)

    return revers_numbers(n)


check_memory(12345678901234787878889900452434536499809797867564534)

"""
При профилировании функции с рекурсией профилировщик запускается при каждом вызове функции.
Если надо посмотреть сколько памяти расходуется на каждом этапе рекурсии, то можно так, если нужен общий
результат, то можно обернуть рекурсивную функцию внешней и профилировать ее.
"""
