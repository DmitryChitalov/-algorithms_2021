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
import cProfile
import timeit


# рекурсия
def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


# Цикл
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


# Срез
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


# метод списка reversed
def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


def main():
    print(f'revers_1 - {timeit.timeit("revers_1(123456)", globals=globals(), number=1000)} сек.')
    print(f'revers_2 - {timeit.timeit("revers_2(123456)", globals=globals(), number=1000)} сек.')
    print(f'revers_3 - {timeit.timeit("revers_3(123456)", globals=globals(), number=1000)} сек.')
    print(f'revers_4 - {timeit.timeit("revers_4(123456)", globals=globals(), number=1000)} сек.')


cProfile.run('main()')

'''
revers_1 - 0.002501400000000001 сек.
revers_2 - 0.0010045999999999944 сек.
revers_3 - 0.0004466999999999943 сек.
revers_4 - 0.0008996000000000004 сек.
         11090 function calls (5086 primitive calls) in 0.006 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 <timeit-src>:2(<module>)
        1    0.000    0.000    0.001    0.001 <timeit-src>:2(inner)
7000/1000    0.002    0.000    0.002    0.000 task_3.py:16(revers_1)
     1000    0.001    0.000    0.001    0.000 task_3.py:27(revers_2)
     1000    0.000    0.000    0.000    0.000 task_3.py:36(revers_3)
     1000    0.000    0.000    0.001    0.000 task_3.py:43(revers_4)
        1    0.000    0.000    0.006    0.006 task_3.py:47(main)
        4    0.000    0.000    0.001    0.000 timeit.py:101(__init__)
        4    0.000    0.000    0.005    0.001 timeit.py:163(timeit)
        4    0.000    0.000    0.006    0.001 timeit.py:230(timeit)
        8    0.000    0.000    0.000    0.000 timeit.py:79(reindent)
       12    0.001    0.000    0.001    0.000 {built-in method builtins.compile}
      5/1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
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

'''
'''
Выводы
timeit и cProfile выдают практически одинаковые результаты (cProfile - округляет)
рекусия работает медленее осталных. Цикл работает в 2 раза быстрее. Наилучшие результаты у среза. Функция  с reversed 
работает медленее среза, по всей вдимиости притормаживают обращения к join

'''