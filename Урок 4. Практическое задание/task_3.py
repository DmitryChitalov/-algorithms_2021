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


def revers_4(num, revers=''):
    if num == 0:
        return revers
    else:
        revers += str(num % 10)
        return revers_4(num // 10, revers)


def memoize(f):
    cache = {}
    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def revers_5(number):
    if number == 0:
        return ''
    return f'{number % 10}{revers_5(number // 10)}'


num = randint(100000000, 10000000000000)


print(f'revers_1= {timeit("revers_1(num)", "from __main__ import revers_1, num", number=10000)}')
print(f'revers_2= {timeit("revers_2(num)", "from __main__ import revers_2, num", number=10000)}')
print(f'revers_3= {timeit("revers_3(num)", "from __main__ import revers_3, num", number=10000)}')
print(f'revers_4= {timeit("revers_4(num)", "from __main__ import revers_4, num", number=10000)}')
print(f'revers_5= {timeit("revers_5(num)", "from __main__ import revers_5, num", number=10000)}')

cProfile.run("revers_1(num), revers_2(num), revers_3(num), revers_4(num), revers_5(num)")

"""
revers_1 - рекурсия оказалась самая медленная и вызывается n-раз (количество цифр в числе)
revers_2 - цикл и переназначение переменных работает долго
revers_3 - меняем тип на str и делаем reverse - сложность O(n) 
revers_4 - я так думаю, что она самая мадленная из-за конкатенации строки + рекурсивный метод
revers_5 - мемоизация (хеширование) оказывается спасает всегда - самая быстрая
"""