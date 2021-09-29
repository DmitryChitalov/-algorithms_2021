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
from timeit import timeit


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num):
    revers_num = 0
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num: int) -> str:
    rev_lst = list(str(enter_num))
    rev_lst.reverse()
    return ''.join(rev_lst)


def revers_5(enter_num: int) -> str:
    str_num = str(enter_num)
    return ''.join([str_num[i] for i in range(len(str_num)-1, 0, -1)])


if __name__ == '__main__':
    num = 12345678
    print()
    run('revers_1(num)')
    print(f"revers_1 time for 1000 executions: {timeit('revers_1(num)', globals=globals(), number=1000)}")
    print('=' * 50)

    """
    РЕКУРСИЯ
             12 function calls (4 primitive calls) in 0.000 seconds

       Ordered by: standard name
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.000    0.000    0.000    0.000 <string>:1(<module>)
          9/1    0.000    0.000    0.000    0.000 task_3.py:21(revers_1)
            1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    
    
    revers_1 time for 1000 executions: 0.0022416999999999992
    ==================================================
    """

    print()
    run('revers_2(num)')
    print(f"revers_2 time for 1000 executions: {timeit('revers_2(num)', globals=globals(), number=1000)}")
    print('=' * 50)

    """
    ЦИКЛ WHILE
             4 function calls in 0.000 seconds

       Ordered by: standard name
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.000    0.000    0.000    0.000 <string>:1(<module>)
            1    0.000    0.000    0.000    0.000 task_3.py:31(revers_2)
            1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    
    
    revers_2 time for 1000 executions: 0.0011429999999999912
    ==================================================
    """

    print()
    run('revers_3(num)')
    print(f"revers_3 time for 1000 executions: {timeit('revers_3(num)', globals=globals(), number=1000)}")
    print('=' * 50)

    """
    СРЕЗ
             4 function calls in 0.000 seconds

       Ordered by: standard name
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.000    0.000    0.000    0.000 <string>:1(<module>)
            1    0.000    0.000    0.000    0.000 task_3.py:39(revers_3)
            1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    
    
    revers_3 time for 1000 executions: 0.00028750000000000997
    ==================================================
    """

    print()
    run('revers_4(num)')
    print(f"revers_4 time for 1000 executions: {timeit('revers_4(num)', globals=globals(), number=1000)}")
    print('=' * 50)

    """
    ВСТРОЕННАЯ ФУНКЦИЯ REVERSE
             6 function calls in 0.000 seconds

       Ordered by: standard name
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.000    0.000    0.000    0.000 <string>:1(<module>)
            1    0.000    0.000    0.000    0.000 task_3.py:45(revers_4)
            1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
            1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
            1    0.000    0.000    0.000    0.000 {method 'reverse' of 'list' objects}
    
    
    revers_4 time for 1000 executions: 0.0006728000000000012
    ==================================================
    """

    print()
    run('revers_5(num)')
    print(f"revers_5 time for 1000 executions: {timeit('revers_5(num)', globals=globals(), number=1000)}")
    print('=' * 50)

    """
    СПИСКОВОЕ ВКЛЮЧЕНИЕ
             7 function calls in 0.000 seconds

       Ordered by: standard name
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.000    0.000    0.000    0.000 <string>:1(<module>)
            1    0.000    0.000    0.000    0.000 task_3.py:51(revers_5)
            1    0.000    0.000    0.000    0.000 task_3.py:53(<listcomp>)
            1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
            1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
            1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
    
    
    revers_5 time for 1000 executions: 0.0017734999999999973
    ==================================================
    """

    """
    Вывод: Самая быстрая функция - func_3, но вряд ли она самая эффективная по памяти, потому что занимает два раза
    память под строку. Самая эффективная по памяти функция func_3, она использует память только для 3-х целочисленных
     переменных. Худшее решение - рекурсия (func_1). Она, во-первых, самая медленная из-за 9 дополнительных вызовов 
     самой себя; во-вторых, она все эти дополнительных 9 раз выделяет память под три своих целочисленных переменных.
     Результат использованной мной функции немного уступает func_3 из-за 2-х лишних преобразований: в список и обратно. 
    """
