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
    if enter_num < 10:
        return str(enter_num)
    else:
        return str(enter_num % 10) + revers_4(enter_num // 10)


def revers_5(enter_num):
    return str(enter_num) if enter_num < 10 else str(enter_num % 10) + revers_5(enter_num // 10)


def revers_6(enter_num):
    return str(enter_num)[::-1]


def revers_7(enter_num):
    lst = []
    lst.extend(str(enter_num))
    lst.reverse()
    revers_num = ''.join(lst)
    return revers_num


num = 12345
print(revers_1(num))
print(timeit("revers_1(num)", globals=globals()))
run('revers_1(num)')

print(revers_2(num))
print(timeit("revers_2(num)", globals=globals()))
run('revers_2(num)')

print(revers_3(num))
print(timeit("revers_3(num)", globals=globals()))
run('revers_3(num)')

print(revers_4(num))
print(timeit("revers_4(num)", globals=globals()))
run('revers_4(num)')

print(revers_5(num))
print(timeit("revers_5(num)", globals=globals()))
run('revers_5(num)')

print(revers_6(num))
print(timeit("revers_6(num)", globals=globals()))
run('revers_6(num)')

print(revers_7(num))
print(timeit("revers_7(num)", globals=globals()))
run('revers_7(num)')

# Функции revers_1(), revers_4() и revers_5() - это рекурсия. Следовательно работать будет очень медленно.
# Функция revers_2() - это цикл. Сложность ниже, чем у рекурсии, поэтому работать будет быстрее.
# Функции revers_3() и revers_6() самые эффективные. <object_name>[<start_index>, <stop_index>, <step>].
# Проходит от конца к началу, возвращая каждый элемент. revers_6() - это revers_3() с уменьшенным количеством операций,
# работает ещё быстрее.
# Функция revers_7() - список. Работает чуть медленнее revers_3() и revers_6(), т.к. происходит преобразование строки
# в список, а потом обратно в строку.
