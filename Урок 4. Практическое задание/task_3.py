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

import cProfile
from timeit import timeit
from random import randint


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


def memo(f):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return wrapper


@memo
def revers_4(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


num = randint(100000000, 10000000000000)
cProfile.run('revers_3(num),revers_2(num),revers_1(num),revers_4(num)')
print('Первая функция рекурсии выполниласб за:', timeit("revers_1(num)", globals=globals()))
print('Втарая функция выполнилась за:', timeit("revers_2(num)", globals=globals()))
print('Третья функция выполнилась за:', timeit("revers_3(num)", globals=globals()))
print('Четвертая функция рекурсия с мемоизацией  выполнилась за:', timeit("revers_4(num)", globals=globals()))

"""
Больше всего времени занимает первая функция так как это рекурсия 
и требует времени на создание стека вызовов и после выполнения операций но если добавить мемоизацию то она 
выполняется быстрее всех остольных так как позволяет пропускать одинаковые вызовы рекурсии(но если все будут уникальны 
то мемоизация будет минусом).
Функция с циклом быстрее простой рекурсии но все же она выполняет много действий.
Функция со срезом самая быстрая потому что она возвращает копию строки с шагом -1.
Интерестно что сProfile видит функцию 4 но ее выполнение считает для функции один хотя названия их разные 
"""
