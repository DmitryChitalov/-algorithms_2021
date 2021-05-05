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
from cProfile import run
from timeit import timeit
from random import randint


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
    return ''.join(list(str(enter_num))[::-1])


num = randint(100000000, 1000000000000)
print('revers_1:', timeit('revers_1(num)', globals=globals(), number=100000))
print('revers_2:', timeit('revers_2(num)', globals=globals(), number=100000))
print('revers_3:', timeit('revers_3(num)', globals=globals(), number=100000))
print('revers_4:', timeit('revers_4(num)', globals=globals(), number=100000))

functions = (revers_1, revers_2, revers_3, revers_4)
for func in functions:
    run('func(randint(100000000, 1000000000000))')

# наиболее эффективным оказался вариант №3
# cProfile тут особо не помогает,
# но можно сравнить кол-во применяемых методов в том или ином алгоритме и количество вызовов функций в общем
