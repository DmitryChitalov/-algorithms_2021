"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit
Обязательно предложите еще свой вариант решения и также запрофилируйте!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""
from cProfile import run
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


def new_revers_1(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{new_revers_1(number // 10)}'


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
    return ''.join(reversed((str(enter_num))))


num_1000 = randint(1000000, 10000000)
print(f'revers_1(num_1000) - {timeit("revers_1(num_1000)", globals=globals())}')
print(f'new_revers_1(num_1000) - {timeit("new_revers_1(num_1000)", globals=globals())}')
print(f'revers_2(num_1000) - {timeit("revers_2(num_1000)", globals=globals())}')
print(f'revers_3(num_1000) - {timeit("revers_3(num_1000)", globals=globals())}')
print(f'revers_4(num_1000) - {timeit("revers_4(num_1000)", globals=globals())}')


test_1 = """
for i in range(1000000):
    revers_1(num_1000)
"""
test_2 = """
for i in range(1000000):
    revers_2(num_1000)
"""
test_3 = """
for i in range(1000000):
    revers_3(num_1000)
"""
test_4 = """
for i in range(1000000):
    revers_4(num_1000)
"""

run(test_1)
print("-" * 100)
run(test_2)
print("-" * 100)
run(test_3)
print("-" * 100)
run(test_4)

"""
Вывод № 1. revers_1 и revers_2 не работают на чилах, оканчивающихся на цифру "0".
Вывод № 2. revers_1, new_revers_1 - самые медленные, т.к. работают через рекурсию 
Вывод № 3. revers_3 - самая быстрая. 
Вывод № 4. revers_4 работает медленнее среза, но быстрее двух остальных, т.к. не
использует циклов
Вывод № 5. Профайлер показывает, что замедление revers_1 вызвано значительным кол-вом 
вызовов рекурсии: ncalls: 8000000/1000000. revers_4 в свою очередь замедляется дополнительным 
вызовом метода join 
"""