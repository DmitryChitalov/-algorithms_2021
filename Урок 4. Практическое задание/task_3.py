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

# В первом случае операция выполняется с помощью рекурсии, во втором - с помощью цикла, в третьем - с помощью среза.
# Сразу можно сказать, что результат реализации с рекурсией займёт больше всего времени.
# Остаются цикл и срез. В цикле выполняются арифметические действия, что само собой занимает время,
# поэтому функция со срезом фактически должна занять меньше времени; что и подтверждается результатами профилирования.


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


print(f'Время реализации функции с рекурсией: {timeit("revers_1(90 ** 100)", globals=globals(), number=1000)}')
run('revers_1(90 ** 100)')


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


print(f'Время реализации функции с циклом: {timeit("revers_2(90 ** 100)", globals=globals(), number=1000)}')
run('revers_2(90 ** 100)')


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


print(f'Время реализации функции с помощью среза: {timeit("revers_3(90 ** 100)", globals=globals(), number=1000)}')
run('revers_3(90 ** 100)')
