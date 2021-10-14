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
from timeit import *
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

def revers_4(n):
    n_list = list(str(n))
    n_list.reverse()
    n2 = "".join(n_list)
    return n2

print(min(repeat("revers_4(2244)", globals=globals(), timer=default_timer , number=100000)))
print(min(repeat("revers_3(2244)", globals=globals(), timer=default_timer , number=100000)))
print(min(repeat("revers_2(2244)", globals=globals(), timer=default_timer , number=100000)))
print(min(repeat("revers_1(2244)", globals=globals(), timer=default_timer , number=100000)))


run('revers_4(2244)')
run('revers_3(2244)')
run('revers_2(2244)')
run('revers_1(2244)')

# третья функция быстрее всех. Наверное потому что мы не делали никаких вычеслений или как я делал строку в лист и обратно

