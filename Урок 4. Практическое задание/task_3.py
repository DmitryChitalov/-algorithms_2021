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
from random import randint
import cProfile

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
    rez = {v: str(enter_num)[v] for v in range(len(str(enter_num)))}
    lst = ''
    for k in range(len(rez)-1, -1, -1):
        lst = lst + rez[k]
    return lst


number = randint(10000, 1000000)
print(number)
print(f' rev_number = {revers_1(number)} => time_1 = {timeit("revers_1(number)", globals=globals())}')
print(f' rev_number = {revers_2(number)} => time_2 = {timeit("revers_2(number)", globals=globals())}')
print(f' rev_number = {revers_3(number)} => time_3 = {timeit("revers_3(number)", globals=globals())}')
print(f' rev_number = {revers_4(number)} => time_4 = {timeit("revers_4(number)", globals=globals())}')

cProfile.run('revers_1(number)')
cProfile.run('revers_2(number)')
cProfile.run('revers_3(number)')
cProfile.run('revers_4(number)')

"""
    Самый эффективный является способ № 3 (revers_3 - реализация через срез), так как сложность данной функции 
не имеет в отличае от других арифметических действий.
"""