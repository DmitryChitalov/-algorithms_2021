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
    enter_num = list(str(enter_num))
    enter_num.reverse()
    return ''.join(enter_num)


# cProfile
def main():
    num = 123456789
    revers_1(num)
    revers_2(num)
    revers_3(num)
    revers_4(num)


run('main()')
num = 123456789

# timeit
print(timeit('revers_1(num)', 'from __main__ import revers_1, num'))
print(timeit('revers_2(num)', 'from __main__ import revers_2, num'))
print(timeit('revers_3(num)', 'from __main__ import revers_3, num'))
print(timeit('revers_4(num)', 'from __main__ import revers_4, num'))


# revers_3 выполняется быстрее т.к. срез быстрее чем цикл или рекурсия
# revers_1 - самый медленный т.к в нем используется стек вызовов
# revers_4 быстрее чем цикл или рекурсия, но медленнее среза
