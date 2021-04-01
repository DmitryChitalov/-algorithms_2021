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
    def count_number(numb, even=0, odd=0):
        if numb == 0:
            return even, odd
        else:
            if (numb % 10) % 2 == 0:
                even += 1
            else:
                odd += 1
        return count_number(numb // 10, even, odd)
    return count_number(number)


print(cnt(2225))
'''Необходимо обернуть рекурсию еще в одну функцию'''
