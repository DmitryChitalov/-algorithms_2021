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

from cProfile import run
from random import randint
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
    list_x = list(str(enter_num))
    list_x.reverse()
    return ''.join(list_x)


def main(enter_num):
    for i in range(10000):
        revers_1(enter_num)
        revers_2(enter_num)
        revers_3(enter_num)
        revers_4(enter_num)


if __name__ == '__main__':
    num = randint(1000000, 1000000000000000)
    run('main(num)')
    print(revers_4(num) == revers_3(num))
    print(f'Время выполнения функции revers_1: {timeit(stmt="revers_1(num)", globals=globals(), number=10000)}')
    print(f'Время выполнения функции revers_2: {timeit(stmt="revers_2(num)", globals=globals(), number=10000)}')
    print(f'Время выполнения функции revers_3: {timeit(stmt="revers_3(num)", globals=globals(), number=10000)}')
    print(f'Время выполнения функции revers_4: {timeit(stmt="revers_4(num)", globals=globals(), number=10000)}')

#  использовать лучше функцию revers_3 так как минимум операций и сложность O(1)
