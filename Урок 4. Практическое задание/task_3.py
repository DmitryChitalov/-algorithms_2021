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
from random import randint
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

num_10000 = randint(100000000, 10000000000000)

print(f'cProfile')
run('revers_1(num_10000) ')
run('revers_2(num_10000)')
run('revers_3(num_10000)')

print('"timeit"')
print('revers_1',end=" ")
print(f'{timeit("revers_1(num_10000)", number=10000, globals=globals())}')
print('revers_2',end=" ")
print(f'{timeit("revers_2(num_10000)", number=10000, globals=globals())}')
print('revers_3',end=" ")
print(f'{timeit("revers_3(num_10000)", number=10000, globals=globals())}')


# функция revers_1 самая медленная так как использует рекурсию
# функция revers_2  быстрее чем revers_1 так использует цикл вместо рекурсии
# функция revers_3 самая быстрая так используется встроенная функция


