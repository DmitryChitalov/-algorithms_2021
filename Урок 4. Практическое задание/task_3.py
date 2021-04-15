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
value = 123456789123456789


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


# удаляю промежуточные переменные, экономлю время и память для их выделения
def revers_4(enter_num):
    return str(enter_num)[::-1]


statements = [
    'revers_1(value)',
    'revers_2(value)',
    'revers_3(value)',
    'revers_4(value)']


for sta in statements:
    print(timeit(sta, globals=globals(), number=1000000))


def main():
    for i in range(1000000):
        revers_1(value)
        revers_2(value)
        revers_3(value)
        revers_4(value)


run("main()")


"""
Выводы. Из предложеных в задании вериантов реверса 3-й оптимальный. Т.к. срез является встроенной
        функцией, да и в целом там выполняется наименьшее число операций.
"""