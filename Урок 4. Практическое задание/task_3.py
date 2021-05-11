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


import timeit
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


numb = 1000000

print('timeit:')
print(f'revers_1: {revers_1(numb)},\t'
      f'{timeit.repeat("revers_1(numb)", "from __main__ import revers_1, numb", repeat=3, number=1000000)} сек.')
print(f'revers_2: {revers_2(numb)},\t'
      f'{timeit.repeat("revers_2(numb)", "from __main__ import revers_2, numb", repeat=3, number=1000000)} сек.')
print(f'revers_3: {revers_3(numb)},\t'
      f'{timeit.repeat("revers_3(numb)", "from __main__ import revers_3, numb", repeat=3, number=1000000)} сек.')

print('cProfile: ')
print(f'revers_1: {revers_1(numb)}:\n: {cProfile.run("revers_1(numb)")}')
print(f'revers_2: {revers_2(numb)}:\n: {cProfile.run("revers_2(numb)")}')
print(f'revers_3: {revers_2(numb)}:\n: {cProfile.run("revers_3(numb)")}')

"""
1. revers_3 - самая быстрая, т.к. используюя срезы 
2. revers_2
3. revers_1 - самая медленная, из-за рекурсии
"""
