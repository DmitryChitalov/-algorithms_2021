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

def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)

############################################################################
numb = 121212121212

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

def all_reverse():
    numb = 12121212121212121212
    revers_1(numb)
    revers_2(numb)
    revers_3(numb)

#################################################################################
print(revers_1(numb))
print(revers_2(numb))
print(revers_3(numb))
print(timeit('revers_1(numb)', 'from __main__ import revers_1, numb'))
print(timeit('revers_2(numb)', 'from __main__ import revers_2, numb'))
print(timeit('revers_3(numb)', 'from __main__ import revers_3, numb'))

run('all_reverse()')

###################################################################################

'''
Функция переворота числа через срез строки выполняется быстрее рекурсивных функций
'''