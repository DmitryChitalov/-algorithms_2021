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
from random import randint
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
    """
    Убираем присваивания, укладываемся в одну строку, несколько быстрее последнего.
    """
    return str(enter_num)[::-1]


number = randint(100000, 99999999999)

run('revers_1(number)')
run('revers_2(number)')
run('revers_3(number)')

print('revers_1:', timeit('revers_1(number)', globals=globals()))
# Самый длительный из-за рекурсии
print('revers_2:', timeit('revers_2(number)', globals=globals()))
# Быстрее т.к. делаем только один проход
print('revers_3:', timeit('revers_3(number)', globals=globals()))
# Самый быстрый из стандартных - берем из строки элементы с обратной стороны
print('revers_4:', timeit('revers_3(number)', globals=globals()))



