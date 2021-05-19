"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
from memory_profiler import profile


@profile
def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


@profile
def outer_revers_1():
    def revers_1(enter_num, revers_num=0):
        if enter_num == 0:
            return revers_num
        else:
            num = enter_num % 10
            revers_num = (revers_num + num / 10) * 10
            enter_num //= 10
            return revers_1(enter_num, revers_num)

print(outer_revers_1())

# Для того, чтобы декоратор не срабатовал на каждом вызове функции, нужно поместить функцию в функцию