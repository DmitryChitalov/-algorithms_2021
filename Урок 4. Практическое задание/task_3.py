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
from random import randint

#
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


# Реверc списка
def revers_4(enter_num):
    num_list = list(str(enter_num))
    num_list.reverse()
    return ''.join(num_list)


# Pop и append в список
def revers_5(enter_num):
    num_list = list(str(enter_num))  # O(n)
    res_list = []
    while num_list:                     # O(n)
        res_list.append(num_list.pop())  # O(1)
    return res_list


# Проверяем результаты и делаем выводы:


# Число для профилиирования
num = 6587795

# Профилируем с timeit
print('revers_1 (рекурсия)', timeit('revers_1(num)', globals=globals(), number=100000))
print('revers_2 (цикл)', timeit('revers_2(num)', globals=globals(), number=100000))
print('revers_3 (срез)', timeit('revers_3(num)', globals=globals(), number=100000))
print('revers_4 (reverse() списка + join())', timeit('revers_4(num)', globals=globals(), number=100000))
print('revers_5 (pop() + append())', timeit('revers_5(num)', globals=globals(), number=100000))


# Профилируем с cProfile
def main(num):
    for i in range(100000):
        revers_1(num)
        revers_2(num)
        revers_3(num)
        revers_4(num)
        revers_5(num)


run(f'main({num})')

"""
Вывод:
Самый эффективный способ revers_3, использующий срез. В данном случае создается копия списка 
без применения операций добавления значений, а также обходов циклами, где нужно еще генерировать последовательность. 
Самые медленные алгоритмы получились revers_1 и revers_5.
В revers_1 используется рекурсия и если посмотреть на результат СProfile, 
то видно, что общее количество вызовов функции, включая рекурсивные, будет в 8 раз больше количетсва 
нерекурсивных вызовов (ncalls = 800000/100000). Т.е. время будет значительное, 
даже при сложности О(1) операций на каждом вызове.
В revers_5 сделано много лишних операций (обратная ситуация срезам) для модификации исходного и нового массивов.  
     
"""

# Результаты замеров:

# revers_1 (рекурсия) 0.2026135
# revers_2 (цикл) 0.14500659999999999
# revers_3 (срез) 0.0537301
# revers_4 (reverse() списка + join()) 0.06313450000000004
# revers_5 (pop() + append()) 0.12753570000000003
#          2800004 function calls (2100004 primitive calls) in 1.290 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.290    1.290 <string>:1(<module>)
# 800000/100000    0.368    0.000    0.368    0.000 task_3.py:21(revers_1)
#    100000    0.160    0.000    0.160    0.000 task_3.py:31(revers_2)
#    100000    0.048    0.000    0.048    0.000 task_3.py:39(revers_3)
#    100000    0.091    0.000    0.126    0.000 task_3.py:46(revers_4)
#    100000    0.287    0.000    0.439    0.000 task_3.py:53(revers_5)
#         1    0.150    0.150    1.290    1.290 task_3.py:72(main)
#         1    0.000    0.000    1.290    1.290 {built-in method builtins.exec}
#    700000    0.070    0.000    0.070    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    100000    0.024    0.000    0.024    0.000 {method 'join' of 'str' objects}
#    700000    0.083    0.000    0.083    0.000 {method 'pop' of 'list' objects}
#    100000    0.011    0.000    0.011    0.000 {method 'reverse' of 'list' objects}
