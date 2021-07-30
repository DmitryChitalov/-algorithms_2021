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

'''Самым эффективным является третий способ, так как идёт работа с константными скоростями и 
без осуществления арифметических операций. Можно ускорить написав код в одну строку. Способ 4 уступает третьему и пятому
в силу того, что просиходит с итерируемым объектом и последующим методом .join. Первый способ более быстрый, чем второй
в силу проверки лишь одного условия из-за отсутвия разветвления через if.'''


from timeit import timeit
from cProfile import run


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
    return ''.join(reversed(str(enter_num)))


def revers_5(enter_num):
    return str(enter_num)[::-1]


num = 12345678901234567890

print('timeit:\n\nrevers_1')
print(
    timeit(
        "revers_1(num)",
        setup='from __main__ import revers_1, num',
        number=100000))
print('revers_2')
print(
    timeit(
        "revers_2(num)",
        setup='from __main__ import revers_2, num',
        number=100000))
print('revers_3')
print(
    timeit(
        "revers_3(num)",
        setup='from __main__ import revers_3, num',
        number=100000))
print('revers_5')
print(
    timeit(
        "revers_5(num)",
        setup='from __main__ import revers_5, num',
        number=100000))
print('revers_4')
print(
    timeit(
        "revers_4(num)",
        setup='from __main__ import revers_4, num',
        number=100000), '\n\ncProfile:\n')
print('revers_1')
print(run('revers_1'))
print('revers_2')
print(run('revers_2'))
print('revers_3')
print(run('revers_3'))
print('revers_4')
print(run('revers_4'))
