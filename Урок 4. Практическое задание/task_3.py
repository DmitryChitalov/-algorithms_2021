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
    """
    Самый медленный вариант. Рекурсия + много вычислений
    """
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    """
    Вариант побыстрее. Потому что без рекурсии.
    """
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    """
    Этот вариант самый быстрый. Здесь используются встроенные возможности Python, что позволяет алгоритму
    выполняться очень быстро.
    """
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    """
    Этот вариант тоже быстрый. По той же причине, что и предыдущий.
    Но здесь больше преобразований, поэтому уступает в скорости.
    """
    num_list = list(str(enter_num))
    num_list.reverse()
    return "".join(num_list)


en_num = 45678905678789
print("Замеры времени с помощью timeit:")
print(timeit("revers_1(en_num)", globals=globals(), number=1000))
print(timeit("revers_2(en_num)", globals=globals(), number=1000))
print(timeit("revers_3(en_num)", globals=globals(), number=1000))
print(timeit("revers_4(en_num)", globals=globals(), number=1000))
"""
Замеры времени с помощью timeit:
0.008031299999999991
0.0040363999999999955
0.00039300000000000446
0.0010787999999999909
"""

"""
Замеры с помощью сProfile здесь не эффективны, так как все функции очень быстрые.
"""
def main():
    enter_num = 45678905678789
    num1 = revers_1(enter_num)
    num2 = revers_2(enter_num)
    num3 = revers_3(enter_num)
    num4 = revers_4(enter_num)

print("\nЗамеры времени с помощью cProfile:")
run('main()')

"""
 24 function calls (10 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     15/1    0.000    0.000    0.000    0.000 task_3.py:21(revers_1)
        1    0.000    0.000    0.000    0.000 task_3.py:34(revers_2)
        1    0.000    0.000    0.000    0.000 task_3.py:45(revers_3)
        1    0.000    0.000    0.000    0.000 task_3.py:55(revers_4)
        1    0.000    0.000    0.000    0.000 task_3.py:75(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'reverse' of 'list' objects}

"""