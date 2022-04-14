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
import cProfile

"""
revers_1 и revers_2
возвращает float, код изменила
"""


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, int(revers_num))


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = int((revers_num + num / 10) * 10)
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def my_revers(enter_num):
    revers_num = list(str(enter_num))
    revers_num.reverse()
    return ''.join(revers_num)


num = 125890250


def my_timeit():
    print(timeit('revers_1(num)', globals=globals()))
    print(timeit('revers_2(num)', globals=globals()))
    print(timeit('revers_3(num)', globals=globals()))
    print(timeit('my_revers(num)', globals=globals()))


my_timeit()

"""
3.5316249890020117
2.6158319619717076
0.3712243320187554
0.6514093090081587

самя эффективная функция revers_3, использует встроенную возможность среза с отрицательным шагом
чуть хуже моя функция за счет двойно работы - из строки в список, переворот и обратно из списка в строку
"""

cProfile.run('my_timeit()')

"""
5.175073113990948
2.813345858012326
0.5201931819901802  
1.1104450800339691
         15000090 function calls (6000086 primitive calls) in 9.031 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    9.620    9.620 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 <timeit-src>:2(<module>)
        1    0.196    0.196    1.110    1.110 <timeit-src>:2(inner)
        
  __________________________________________________________________________      
10000000/1000000    4.947    0.000    4.947    0.000 task_3.py:26(revers_1)
  1000000    2.628    0.000    2.628    0.000 task_3.py:36(revers_2)
  1000000    0.345    0.000    0.345    0.000 task_3.py:44(revers_3)
  1000000    0.674    0.000    0.915    0.000 task_3.py:50(my_revers)
  
  cProfile также показывает примерно те же цифры и указывает на revers_3
  как на самую эффективную и быструю функцию.
  А revers_1 - самая тяжелая функция. Это подтверждает и О-нотация:
  revers_1 - O(n**2)
  revers_2 - O(n)
  revers_3 - O(n)
  my_revers- O(n)
  __________________________________________________________________________
        1    0.000    0.000    9.620    9.620 task_3.py:59(my_timeit)
        4    0.000    0.000    0.001    0.000 timeit.py:101(__init__)
        4    0.000    0.000    9.619    2.405 timeit.py:163(timeit)
        4    0.000    0.000    9.620    2.405 timeit.py:230(timeit)
        8    0.000    0.000    0.000    0.000 timeit.py:79(reindent)
       12    0.001    0.000    0.001    0.000 {built-in method builtins.compile}
      5/1    0.000    0.000    9.620    9.620 {built-in method builtins.exec}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.globals}
        8    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        4    0.000    0.000    0.000    0.000 {built-in method gc.disable}
        4    0.000    0.000    0.000    0.000 {built-in method gc.enable}
        4    0.000    0.000    0.000    0.000 {built-in method gc.isenabled}
        8    0.000    0.000    0.000    0.000 {built-in method time.perf_counter}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        4    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
  1000000    0.170    0.000    0.170    0.000 {method 'join' of 'str' objects}
        8    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
  1000000    0.071    0.000    0.071    0.000 {method 'reverse' of 'list' objects}



Process finished with exit code 0

"""