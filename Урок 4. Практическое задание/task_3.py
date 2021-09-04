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

import timeit
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


def my_revers(enter_num):
    my_list = list(str(enter_num))
    my_list.reverse()
    ''.join(my_list)


my_num = 123456789

print(timeit.timeit('revers_1(my_num)', globals=globals(), number=1000))
print(timeit.timeit('revers_2(my_num)', globals=globals(), number=1000))
print(timeit.timeit('revers_3(my_num)', globals=globals(), number=1000))
print(timeit.timeit('my_revers(my_num)', globals=globals(), number=1000))


def main():
    revers_1(my_num)
    revers_2(my_num)
    revers_3(my_num)
    my_revers(my_num)


run('main()')

"""
Вывод: по результатам замеров наиболее эффективным является решение через срез, затем предложенный способ через метод 
revers, значительно дольше решение через цикл, дольше всего решение через рекурсию.
"""
