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
from cProfile import run
from random import randint

num = randint(10000, 100000)

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


# еще вариант:
def revers_4(enter_num):
    enter_num = str(enter_num)
    return ''.join([l for l in reversed(enter_num)])


for f in [f'revers_{n}(num)' for n in range(1, 5)]:
    print(f'{f}:', timeit(f, globals=globals(), number=100000))
    run(f)


# revers_1(num): 0.2530349
# revers_2(num): 0.18406950000000005
# revers_3(num): 0.052933999999999926
# revers_4(num): 0.13425759999999998

# Метод с использованием рекурсии (revers_1) оказался самым медленным, потому что для пятизначного числа требуется
# шесть вызовов функции, что мы видим из сProfile:
# 6/1    0.000    0.000    0.000    0.000 task_3.py:23(revers_1)

# Функция 2 - это функция номер один, но написанная через цикл вместо рекурсии, поэтому занимает меньше времени.

# Третья функция значительно быстрее двух предыдущих: 0.052 против 0.253 и 0.184, потому что использует встроенные
# методы: обращение числа в строку и слайсинг.

# Четвертая функция по скорости на втором месте, однако тоже является медленной, потому что использует reverse (O(n))
# и итерацию по всему листу (O(n)).
