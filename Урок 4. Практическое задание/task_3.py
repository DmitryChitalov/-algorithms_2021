"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
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
    return revers_num


def main():
    num = 1234567
    revers_1(num)
    revers_2(num)
    revers_3(num)


my_num = 1234567

print('Профилировка через "timeit":')
print(timeit("revers_1(my_num)", globals=globals()))
print(timeit("revers_2(my_num)", globals=globals()))
print(timeit("revers_3(my_num)", globals=globals()))
print()

"""
Самой эффективной здесь является третья реализация, так как в ней не тратится время 
ни на какие вычисления - их просто нет, а только берется срез.
"""


print('Профилировка через "cProfile":')
run('main()')

"""
Профилировка показала, что зедсь функция revers_1 вызывает сама себя (len(num) + 1) раз.
В остальном слабых мест нет.
"""