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
    return revers_num


def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


def main():
    print(f"revers_1(1234): {timeit('revers_1(1234)', globals=globals(), number=1000)}")
    print(f"revers_2(1234): {timeit('revers_2(1234)', globals=globals(), number=1000)}")
    print(f"revers_3(1234): {timeit('revers_3(1234)', globals=globals(), number=1000)}")
    print(f"revers_3(1234): {timeit('revers_4(1234)', globals=globals(), number=1000)}")


run('main()')

"""
timeit:
revers_1(1234): 0.0010454000000000019
revers_2(1234): 0.0006301000000000015
revers_3(1234): 0.0003174000000000024
revers_3(1234): 0.0005743999999999957

cProfile
ncalls       tottime  percall  cumtime  percall     filename:lineno(function)
5000/1000    0.002    0.000    0.002    0.000       task_3.py:20(revers_1)
     1000    0.001    0.000    0.001    0.000       task_3.py:30(revers_2)
     1000    0.000    0.000    0.000    0.000       task_3.py:38(revers_3)
     1000    0.000    0.000    0.001    0.000       task_3.py:44(revers_4)

И timeit и cProfile дают одинаковые результаты: самая эффективная функция - 3, работающая
через срезы. Имеет минимальную сложность. Самое длительное время имеет реализация через рекурсию.
Однако timeit информативнее: дает понять разницу между 2 и 4 реализациями.
"""
