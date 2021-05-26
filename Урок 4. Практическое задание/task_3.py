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
    n_list = list(str(enter_num))
    n_list.reverse()
    revers_num = "".join(n_list)
    return revers_num


print(
    timeit(
        "revers_1(123456789)",
        globals=globals(),
        number=1000))
print(
    timeit(
        "revers_2(123456789)",
        globals=globals(),
        number=1000))
print(
    timeit(
        "revers_3(123456789)",
        globals=globals(),
        number=1000))
print(
    timeit(
        "revers_4(123456789)",
        globals=globals(),
        number=1000))

run('revers_1(123456789)')
run('revers_2(123456789)')
run('revers_3(123456789)')
run('revers_4(123456789)')

# Функция использующая срез работает быстрее так как она является линейной.
# Профилирование показывает, что при выполнении алгоритма со срезом
# происходит вызов четырёх функций, тогда как при выполнении остальных происходит
# шесть вызовов.
