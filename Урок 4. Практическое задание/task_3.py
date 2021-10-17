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
from timeit import Timer
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

def revers_4(enter_num, revers_num = ''):
    enter_num = str(enter_num)
    for i in range(len(enter_num)):
        revers_num = revers_num + enter_num[(len(enter_num) - 1 ) - i]
    return revers_num


t1 = Timer("revers_1(123456789012345678901234567890)", "from __main__ import revers_1")
print("list revers_1 ", t1.timeit(number=1000), "milliseconds")
run('revers_1')

t2 = Timer("revers_2(123456789012345678901234567890)", "from __main__ import revers_2")
print("list revers_2 ", t2.timeit(number=1000), "milliseconds")
run('revers_2')

t3 = Timer("revers_3(123456789012345678901234567890)", "from __main__ import revers_3")
print("list revers_3 ", t3.timeit(number=1000), "milliseconds")
run('revers_3')

t4 = Timer("revers_4(123456789012345678901234567890)", "from __main__ import revers_4")
print("list revers_4 ", t4.timeit(number=1000), "milliseconds")
run('revers_4')
'''
revers_3 - самая быстрая функция т.к. выполняется с помощью среза O(b-a).
revers_2 - на втором месте (если небольшое 'n'): цикл WHILE пока число не будет равно нулю O(n)
revers_4 - цикл FOR IN также похож на цикл while со сложностью O(n)
revers_1 -  это рекурсивная функция с экспоненциальной сложностью  - самая медленная O(2^n)
'''