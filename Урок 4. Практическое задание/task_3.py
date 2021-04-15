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
from random import randint
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
    enter_num = str(enter_num)
    revers_num = ''.join(reversed(enter_num))
    return revers_num


num = randint(10000000000000, 100000000000000)
print(num)

print('cProfile')

run('revers_1(num)')
run('revers_2(num)')
run('revers_3(num)')
run('revers_4(num)')

print('timeit')
print('revers_1',
    timeit(
        "revers_1(num)",
        setup='from __main__ import revers_1, num',
        number=10000))
print('revers_2',
    timeit(
        "revers_2(num)",
        setup='from __main__ import revers_2, num',
        number=10000))
print('revers_3',
    timeit(
        "revers_3(num)",
        setup='from __main__ import revers_3, num',
        number=10000))
print('revers_4',
    timeit(
        "revers_4(num)",
        setup='from __main__ import revers_4, num',
        number=10000))

"""
1 - рекурсия наиболее затратный с точки зрения ресурсов вариант, выполняется дольше всего
2 - цикл while работает быстрее рекурсии. Обычно алгоритмы выполненые через рекурсию можно заменить на
    аналогичный вариант с использованием цикла. С точки зрения производительности циклы работают быстрее
3 - используется срез - самый быстрый вариант т.к. это хорошо оптимизированная встроенная возможность языка
4 - еще один вариант, использование встроенных функций reverse() и join(). Выполняется медленнее среза,
    но намного быстрее цикла и рекурсии
"""
