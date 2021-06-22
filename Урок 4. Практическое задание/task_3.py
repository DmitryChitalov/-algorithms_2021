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
from timeit import Timer
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


def revers_4(enter_num):
    num_str = ''
    for i in str(enter_num):
        num_str = i + num_str
    return num_str


num_n = randint(1000000000000000, 9999999999999999)

t1 = Timer("revers_1(num_n)", "from __main__ import revers_1, num_n")
print(f'Суммарное время 10000 запусков revers_1 {t1.timeit(number=10000):.6f} сек')
print('*' * 6)
t2 = Timer("revers_2(num_n)", "from __main__ import revers_2, num_n")
print(f'Суммарное время 10000 запусков revers_2 {t2.timeit(number=10000):.6f} сек')
print('*' * 6)
t3 = Timer("revers_3(num_n)", "from __main__ import revers_3, num_n")
print(f'Суммарное время 10000 запусков revers_3 {t3.timeit(number=10000):.6f} сек')
print('*' * 6)
t4 = Timer("revers_4(num_n)", "from __main__ import revers_4, num_n")
print(f'Суммарное время 10000 запусков revers_4 {t4.timeit(number=10000):.6f} сек')
print('*' * 6)


def main():
    Timer("revers_1(num_n)", "from __main__ import revers_1, num_n").timeit(number=10000)
    Timer("revers_2(num_n)", "from __main__ import revers_2, num_n").timeit(number=10000)
    Timer("revers_3(num_n)", "from __main__ import revers_3, num_n").timeit(number=10000)
    Timer("revers_4(num_n)", "from __main__ import revers_4, num_n").timeit(number=10000)


run('main()')

'''
1 - эфективнее revers_3 превратить в строку и вывести в обратном порядке встроенными методами - O(n)
2 - потом идёт revers_4 превращение в строку и конкатенация в обратном порядке через цикл
3 - потом идёт revers_2 последовательное превращение единиц,полученных из результата целочисленного деления на 10,
в 0.Х сложение и умножение на 10...  
4 - и на последнем рекурсия revers_1
revers_1 - 170 000 рекурсивных вызова / 10 000 - 0,053 сек
revers_2 - 10 000 вызовов - 0,022 сек
revers_3 - 10 000 вызовов - 0,003 сек
revers_4 - 10 000 вызовов - 0,011 сек
'''