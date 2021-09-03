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


def my_reverse(enter_num):
    return ''.join(reversed(f'{enter_num}'))


def main(num):
    revers_1(num)
    revers_2(num)
    revers_3(num)
    my_reverse(num)


NUMBER = randint(100000, 100000000)
print('revers_1 -',
      timeit('revers_1(NUMBER)', globals=globals(), number=100000))
print('revers_2 -',
      timeit('revers_2(NUMBER)', globals=globals(), number=100000))
print('revers_3 -',
      timeit('revers_3(NUMBER)', globals=globals(), number=100000))
print('my_reverse -',
      timeit('my_reverse(NUMBER)', globals=globals(), number=100000))

run('main(NUMBER)')

# Самая эффективная - reverse 3, потому что она самая быстрая.
# reverse_1 - рекурсивная, всем известно что рекурсии медленные
# reverse_2 - много переменных и вычислений
# my_reverse - тратится время на преобразование итератора в строку,
# зато самое краткое решение
