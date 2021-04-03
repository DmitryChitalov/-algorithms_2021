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
    revers_list = list(reversed(str(enter_num)))
    return ''.join(revers_list)

num = 1234567899077653567899876544

print(timeit('revers_1(num)', globals=globals()))
print(timeit('revers_2(num)', globals=globals()))
print(timeit('revers_3(num)', globals=globals()))
print(timeit('revers_4(num)', globals=globals()))
# 6.448772271999999
# 4.538711280000001
# 0.3278988139999992
# 0.8325878960000015


run('revers_1(num)')
run('revers_2(num)')
run('revers_3(num)')
run('revers_4(num)')

# Видим что профилировщик показывает что слабых мест нет и все показатели у всех функций по нулям.
# При этом timeit показывает разницу во времени выпоненения. Самый быстрый через срез, потом с реверсом списка(моя реализация revers_4()), потом цикл, рекурсия дольше всех.
# Это значит что нужно применять оба метода для оптимизации кода.
