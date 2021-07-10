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

"""
Каждый последующий вариант реверса все лучше и лучше (кроме моего)
Рекурсия как и говорили красиво смотрится, но медленно работает
Второй вариант - это цикл и линейная сложность
Третий вариант из всех этих - самый быстрый, потому что работает на срезе -
говорили на уроке что для списков это быстрее всего

Мой вариант дольше из-за джойна наверное... по идее все остальное - стандлартные встроенные методы
"""


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
    return "".join(reversed(str(enter_num)))


def total(enter_num):
    r1 = revers_1(ent_num)
    r2 = revers_2(ent_num)
    r3 = revers_3(ent_num)
    r4 = revers_4(ent_num)

ent_num = 123456789


print("Оценка через timein")
print(
    timeit(
        'revers_1(ent_num, revers_num=0)',
        setup='from __main__ import revers_1, ent_num',
        number=10000))

print(
    timeit(
        'revers_2(ent_num, revers_num=0)',
        setup='from __main__ import revers_2, ent_num',
        number=10000))

print(
    timeit(
        'revers_3(ent_num)',
        setup='from __main__ import revers_3, ent_num',
        number=10000))

print(
    timeit(
        'revers_4(ent_num)',
        setup='from __main__ import revers_4, ent_num',
        number=10000))

print()
run('total(ent_num)')
