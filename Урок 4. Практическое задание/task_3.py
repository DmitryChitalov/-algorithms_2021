#!/usr/bin/env python3

from timeit import timeit
from cProfile import run

num = 1234567890

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
    result = list(str(enter_num))
    result.reverse()
    return ''.join(result)


def revers_5(enter_num):
    l = list(str(enter_num))
    list_len = len(l)
    for i in range(int(list_len / 2)):
        l[i], l[list_len - 1 - i] = l[list_len - 1 - i], l[i]
    return ''.join(l)


def main():

    data = list()
    data.append(('revers_1', timeit("revers_1(num)", globals=globals(), number=10000)))
    data.append(('revers_2', timeit("revers_2(num)", globals=globals(), number=10000)))
    data.append(('revers_3', timeit("revers_3(num)", globals=globals(), number=10000)))
    data.append(('revers_4', timeit("revers_4(num)", globals=globals(), number=10000)))
    data.append(('revers_5', timeit("revers_5(num)", globals=globals(), number=10000)))

    for func, time in sorted(data, key=lambda x : x[1]):
        print(f'{func}: {time}')

if __name__ == '__main__':
    run('main()')


'''
revers_3: 0.007309648000955349
revers_4: 0.011498126999867964
revers_5: 0.024199117000534898
revers_2: 0.02838858299946878
revers_1: 0.06360776099973009

Самыми быстрыми являются способ разворота числа через срез и встроенную функцию sorted т.к. они оптимизированы под быстрое выполнение
Самым медленным в данном случае является рекурсия из за своей алгоритмической сложности.

'''
