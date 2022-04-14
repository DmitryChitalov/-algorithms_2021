"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""
from timeit import timeit
from cProfile import run
from random import randint

enter_num = randint(1000, 1000000)

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
    enter_num = str(enter_num)
    res=int(''.join(reversed(enter_num)))
    return res

print('revers_1')
print(
    timeit(
        "revers_1(enter_num, revers_num=0)",
        setup='from __main__ import revers_1, enter_num',
        number=10000))

print('revers_2')
print(
    timeit(
        "revers_2(enter_num, revers_num=0)",
        setup='from __main__ import revers_2, enter_num',
        number=10000))

print('revers_3')
print(
    timeit(
        "revers_3(enter_num)",
        setup='from __main__ import revers_3, enter_num',
        number=10000))

print('revers_4')
print(
    timeit(
        "revers_4(enter_num)",
        setup='from __main__ import revers_4, enter_num',
        number=10000))


run('revers_1(enter_num)')
run('revers_2(enter_num)')
run('revers_3(enter_num)')
run('revers_4(enter_num)')
"""
Вывод: Cтатистка cProfile не чего нам не дает, так как функция вызываеться один раз и время срабатывания 0,000сек.
Но исходя данных из модуля timeit видно что самым удачным по времени работы являеться функция 3 (получение обратного порядка метотом среза),
далее идет предложения мной функция 4 (использование встроенной функции reversed()), а далее уже идет функция 2 (цикл) и функция 1 (математические операции)
"""

