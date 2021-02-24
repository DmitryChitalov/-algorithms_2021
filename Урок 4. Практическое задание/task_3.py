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

from cProfile import run
from timeit import Timer


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


def revers_4(enter_num):  # моя версия функции реверс
    enter_num = str(enter_num)
    revers_num = ''.join(reversed(enter_num))
    return int(revers_num)


def main():
    timer_1 = Timer("revers_1(12345)", "from __main__ import revers_1")
    timer_1.timeit(number=1000000)
    timer_2 = Timer("revers_2(12345)", "from __main__ import revers_2")
    timer_2.timeit(number=1000000)
    timer_3 = Timer("revers_3(12345)", "from __main__ import revers_3")
    timer_3.timeit(number=1000000)
    timer_4 = Timer("revers_4(12345)", "from __main__ import revers_4")
    timer_4.timeit(number=1000000)


run('main()')


'''
Результаты тестов модуль cProfile на моём пк:
10000082 function calls (5000078 primitive calls) in 2.807 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
6000000/1000000    1.359    0.000    1.359    0.000 task_3.py:20(revers_1)
  1000000    0.604    0.000    0.604    0.000 task_3.py:30(revers_2)
  1000000    0.203    0.000    0.203    0.000 task_3.py:38(revers_3)
  1000000    0.355    0.000    0.528    0.000 task_3.py:43(revers_4)
'''


timer1 = Timer("revers_1(12345)", "from __main__ import revers_1")
print('revers_1', timer1.timeit(number=1000000))
print()
timer2 = Timer("revers_2(12345)", "from __main__ import revers_2")
print('revers_2', timer2.timeit(number=1000000))
print()
timer3 = Timer("revers_3(12345)", "from __main__ import revers_3")
print('revers_3', timer3.timeit(number=1000000))
print()
timer4 = Timer("revers_4(12345)", "from __main__ import revers_4")
print('revers_4', timer4.timeit(number=1000000))


'''
Результаты тестов модуль timeit на моём пк:
revers_1 0.8529198410014942
revers_2 0.5989749839991418
revers_3 0.22920339799929934
revers_4 0.4509231899992301

Вывод по тесту timeit:
Тут опираюсь просто на показатели времени
Быстрейшая функция - revers_3
Второе место - revers_4
Третье место - revers_2
Четвёртое место - revers_1

Вывод по тесту cProfile:
Тут опираюсь на показатель tottime(время потраченное в данной функции)
и на cumtime совокупное время, потраченное как в данной функции, так и 
наследуемых функциях.
Быстрейшая функция - revers_3
Второе место - revers_4
Третье место - revers_2
Четвёртое место - revers_1

Общий вывод таков что встроенные функции и срезы работают быстрее чем 
математические операции с условиями и циклами. Так же использование срезов и
встроенных функций компактнее с меньшим колличеством переменных и строк. Это
делает код более простым для написания. Таким образом код становится проще
для понимания, компактнее и быстрее в исполнении и написании.
'''
