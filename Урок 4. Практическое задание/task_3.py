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
    return int(revers_num)  # пофикшенo - эта функция возвращала строку


def my_revers(enter_num):
    return int(''.join(reversed(str(enter_num))))


def main():
    for i in range(100000):
        revers_1(my_num)
        revers_2(my_num)
        revers_3(my_num)
        my_revers(my_num)


my_num = 7239232574561345732356567345252143437864
print(timeit('revers_1(my_num)', globals=globals(), number=10000))
print(timeit('revers_2(my_num)', globals=globals(), number=10000))
print(timeit('revers_3(my_num)', globals=globals(), number=10000))
print(timeit('my_revers(my_num)', globals=globals(), number=10000))

run('main()')

'''
    Ожидаемо рекурсивная функция самая медленная, функция с перестановками быстрее на порядок, 
    операция со строками быстрее в пять раз, манипуляция со срезами вне конкуренции - быстрее еще в два раза 
'''