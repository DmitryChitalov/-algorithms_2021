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

num = 123456789


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
    revers_num = ''.join(reversed(str(enter_num)))
    return revers_num


print('revers_1:')
print(revers_1(num))
print(timeit('revers_1(num)', globals=globals(), number=1000))
run('revers_1(num)')
print('revers_2:')
print(revers_2(num))
print(timeit('revers_2(num)', globals=globals(), number=1000))
run('revers_2(num)')
print('revers_3:')
print(revers_3(num))
print(timeit('revers_3(num)', globals=globals(), number=1000))
run('revers_3(num)')
print('revers_4:')
print(revers_4(num))
print(timeit('revers_4(num)', globals=globals(), number=1000))
run('revers_4(num)')


# 987654321.0
# 0.0040707  через рекурсию.
# 987654321.0
# 0.0029067999999999976  через цикл
# 987654321
# 0.0003959000000000046  через срез
# 987654321
# 0.0010010999999999978  через встроенную функцию reversed и join
# Самой быстрой оказалась функция, использующая срез, это можно объяснить тем, что:
# 1. ее сложность линейная ( у revers_1 она экспоненциальная)
# 2. работа происходит со строкой.
# 3. отсутствуют дополнительные вызовы, как у revers_4.
# По профилированию с использованием cProfile - у всех функций, кроме последней по четыре примитивных вызова.
# У revers_4 - таких вызовов пять, что обусловлено дополнительным вызовом join для склеивания символов.
# revers_1 - самая медленная из-за большого количества внутрених вызовов функции.

