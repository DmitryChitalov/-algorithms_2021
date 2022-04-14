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
    n_list = list(str(enter_num))
    n_list.reverse()
    revers_num = "".join(n_list)
    return revers_num


num = 1234567890

def main():
    print(f"revers_1(num): {timeit('revers_1(num)', globals=globals(), number=1000)}")
    print(f"revers_2(num): {timeit('revers_2(num)', globals=globals(), number=1000)}")
    print(f"revers_3(num): {timeit('revers_3(num)', globals=globals(), number=1000)}")
    print(f"revers_4(num): {timeit('revers_4(num)', globals=globals(), number=1000)}")


run('main()')
print(revers_1(num))
print(revers_2(num))
print(revers_3(num))
print(revers_4(num))

"""
revers_1(num): 0.007629900000000002
revers_2(num): 0.004663800000000003
revers_3(num): 0.001071500000000003
revers_4(num): 0.0026583999999999983
         16090 function calls (6086 primitive calls) in 0.019 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     1000    0.004    0.000    0.004    0.000 1.py:14(revers_2)
     1000    0.001    0.000    0.001    0.000 1.py:22(revers_3)
     1000    0.002    0.000    0.002    0.000 1.py:27(revers_4)
        1    0.000    0.000    0.020    0.020 1.py:36(main)
11000/1000    0.007    0.000    0.007    0.000 1.py:4(revers_1)
        1    0.000    0.000    0.020    0.020 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 <timeit-src>:2(<module>)
        1    0.000    0.000    0.003    0.003 <timeit-src>:2(inner)
        4    0.000    0.000    0.003    0.001 timeit.py:101(__init__)
        4    0.000    0.000    0.016    0.004 timeit.py:163(timeit)
        4    0.000    0.000    0.020    0.005 timeit.py:230(timeit)
        8    0.000    0.000    0.000    0.000 timeit.py:79(reindent)
       12    0.003    0.000    0.003    0.000 {built-in method builtins.compile}
      5/1    0.000    0.000    0.020    0.020 {built-in method builtins.exec}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.globals}
        8    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        4    0.000    0.000    0.000    0.000 {built-in method gc.disable}
        4    0.000    0.000    0.000    0.000 {built-in method gc.enable}
        4    0.000    0.000    0.000    0.000 {built-in method gc.isenabled}
        8    0.000    0.000    0.000    0.000 {built-in method time.perf_counter}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        4    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
     1000    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        8    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
     1000    0.000    0.000    0.000    0.000 {method 'reverse' of 'list' objects}


987654321.0
987654321.0
0987654321
0987654321



3 функция выполняется быстрее остальных, первые 2 функции некорректно работают
если число заканчивается на 0"""