"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""

import cProfile
from timeit import timeit


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return str(enter_num)[::-1]


num = 12345678910

print(f'1 -- {timeit("revers_1(num)", "from __main__ import revers_1, num", number=1000)}')  # -> 0.0032644000000000006
print(f'2 -- {timeit("revers_2(num)", "from __main__ import revers_2, num", number=1000)}')  # -> 0.002027000000000001
print(f'3 -- {timeit("revers_3(num)", "from __main__ import revers_3, num", number=1000)}')  # -> 0.0003512000000000029
print(f'4 -- {timeit("revers_4(num)", "from __main__ import revers_4, num", number=1000)}')  # -> 0.0003357000000000013

cProfile.run('revers_1(num)')
cProfile.run('revers_2(num)')
cProfile.run('revers_3(num)')
cProfile.run('revers_4(num)')

"""
cProfile не показал каких-либо измерений, только указал на количество вызовов рекурсивной функции
Самая долгая функция - revers_1, так как она вызвается n раз или (len(num)
revers_2 замедляется из-за перебора элементов
Самой эффективной оказалась revers_3, так как в ней используются встроенные методы, а не изобретается колесо.
Но и эту функцию можно улучшить, достаточно убрать шаги с сохранением значений - revers_4
"""
