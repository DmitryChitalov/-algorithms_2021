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


numb = randint(10 ** 200, 10 ** 300)
print(numb)


def revers_1(enter_num, revers_num=0):
    """С увеличением числа происходит сильное замедление
    работы функции, так как функция имеет O(n)"""
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    """Цикл имеет среднее время выполнения,
    но имеется множество переменных и длинных
    математических выражений, также как у
    первой функции от увеличения входного числа
    замедляется быстродействие"""
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    """Функция имеет быстрое время выполнения,
    но создает новый объект revers_num"""
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    """Функция имеет самое быстрое время выполнения,
    использование встроенных функции позволяет написать
    решение в одну строку, а также оптимизировать время выполнения"""
    enter_num = reversed(str(enter_num))
    return enter_num


print('Реверс 1')
print(timeit('revers_1(numb)', globals=globals(), number=10000))
print(run('revers_1(numb)'))
print('*' * 20 + '\n')


print('Реверс 2')
print(timeit('revers_2(numb)', globals=globals(), number=10000))
print(run('revers_2(numb)'))
print('*' * 20 + '\n')


print('Реверс 3')
print(timeit('revers_3(numb)', globals=globals(), number=10000))
print(run('revers_3(numb)'))
print('*' * 20 + '\n')

print('Реверс 4')
print(timeit('revers_4(numb)', globals=globals(), number=10000))
print(run('revers_4(numb)'))
print('*' * 20 + '\n')

