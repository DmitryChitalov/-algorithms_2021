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
    lst = []
    lst.extend(enter_num)
    lst.reverse()
    revers_num = ''.join(lst)
    return revers_num


NUM = 1234567890

print(f'Рекурсия: {NUM} ==> {revers_1(NUM)}')
print(timeit("revers_1(NUM)", globals=globals(), number=1000))
run('revers_1(NUM)')

print(f'Цикл: {NUM} ==> {revers_2(NUM)}')
print(timeit("revers_2(NUM)", globals=globals(), number=1000))
run('revers_2(NUM)')

print(f'Строка: {NUM} ==> {revers_3(NUM)}')
print(timeit("revers_3(NUM)", globals=globals(), number=1000))
run('revers_3(NUM)')

print(f'Список: {NUM} ==> {revers_4(NUM)}')
print(timeit("revers_4(NUM)", globals=globals(), number=1000))
run('revers_4(NUM)')

"""
Рекурсия самая медленная.
Цикл ощутимо быстрее рекурсии, но медленнее остальных вариантов.
Строка самая быстрая.
Список немного медленнее строки, т.к. требует преобразований строки в список и обратно.
"""
