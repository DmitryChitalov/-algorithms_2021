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

import cProfile
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
    revers_num = ''
    for el in reversed(str(enter_num)):
        revers_num += el
    return revers_num


n = 10000
num = 1234567890
print(timeit("revers_1(num)", number=n, globals=globals()))
print(timeit("revers_2(num)", number=n, globals=globals()))
print(timeit("revers_3(num)", number=n, globals=globals()))
print(timeit("revers_4(num)", number=n, globals=globals()))


cProfile.run('for i in range(n):revers_1(num)')
cProfile.run('for i in range(n):revers_2(num)')
cProfile.run('for i in range(n):revers_3(num)')
cProfile.run('for i in range(n):revers_4(num)')

'''
Первая функция, выполненая при помощи рекурсии, ожидаемо выполняется дольще всех,
На третьем месте функция №2, выполненая при помощи цикла while, такая скорость обуславливается множеством лишних 
операций, которых можно избежать при помощи срезов примененных в третьей функции. 
Второе место у функции №4. Она немного проигрывает за счет применения цикла for и конкатенации. 
Первое место у функуии №3.
'''
