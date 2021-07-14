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


def my_revers(enter_num,result=None):
    if result is None:
        result = ''
    if enter_num < 0:
        return result
    if enter_num > 0:
        result += str(enter_num % 10)
    if enter_num == 0:
        return result
    return my_revers(enter_num//10,result)

def main():
    num = 12345
    rev_1 = revers_1(num)
    rev_2 = revers_2(num)
    rev_3 = revers_3(num)
    rev_4 = my_revers(num)


enter_num = 12345
print(f'revers_1 {timeit("revers_1",globals=globals(),number = 1000000)} sec')
print(f'revers_2 {timeit("revers_2",globals=globals(),number = 1000000)} sec')
print(f'revers_3 {timeit("revers_3",globals=globals(),number = 1000000)} sec')
print(f'my_revers_3 {timeit("my_revers",globals=globals(),number = 1000000)} sec')
run('main()')

"""
В качестве своего варианта использовал решение 3-ей задачи из 2-го урока.
Когда мы сравниваем скорость исполнения через timeit и run с количеством 
запуска кода равным 1 (number = 1 и run запускается 1 раз), получается,что
скорость выполнения всех вариантов кода сравнима.

revers_1 1.1299999999991872e-05 sec
revers_2 1.799999999996249e-06 sec
revers_3 1.8000000000240046e-06 sec
my_revers_3 1.500000000015378e-06 sec
         18 function calls (8 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      6/1    0.000    0.000    0.000    0.000 task_3.py:19(revers_1)
        1    0.000    0.000    0.000    0.000 task_3.py:29(revers_2)
        1    0.000    0.000    0.000    0.000 task_3.py:37(revers_3)
      6/1    0.000    0.000    0.000    0.000 task_3.py:43(my_revers)
        1    0.000    0.000    0.000    0.000 task_3.py:54(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

Если же number = 1000, а внутри функции main() мы вызываем все 4 функции через цикл for 
с количеством раз исполнения также равным 1000
(
def main():
    num = 12345
    for i in range(1000):
        rev_1 = revers_1(num)
        rev_2 = revers_2(num)
        rev_3 = revers_3(num)
        rev_4 = my_revers(num)
        
)
то результаты будут следующие:

revers_1 8.139999999999536e-05 sec
revers_2 7.139999999999924e-05 sec
revers_3 7.139999999999924e-05 sec
my_revers_3 7.150000000000212e-05 sec
         14004 function calls (4004 primitive calls) in 0.039 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.039    0.039 <string>:1(<module>)
6000/1000    0.011    0.000    0.011    0.000 task_3.py:19(revers_1)
     1000    0.006    0.000    0.006    0.000 task_3.py:29(revers_2)
     1000    0.002    0.000    0.002    0.000 task_3.py:37(revers_3)
6000/1000    0.016    0.000    0.016    0.000 task_3.py:43(my_revers)
        1    0.004    0.004    0.039    0.039 task_3.py:54(main)
        1    0.000    0.000    0.039    0.039 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

замеры через timeit при number = 1000000
1 замер
revers_1 0.1177462 sec
revers_2 0.0962443 sec
revers_3 0.09521860000000004 sec
my_revers_3 0.09669190000000005 sec

2 замер
revers_1 0.08619310000000002 sec
revers_2 0.10508989999999999 sec
revers_3 0.09977959999999997 sec
my_revers_3 0.09581660000000003 sec

3 замер
revers_1 0.09107130000000001 sec
revers_2 0.08999199999999999 sec
revers_3 0.0715517 sec
my_revers_3 0.08649459999999998 sec

4 замер
revers_1 0.15727329999999998 sec
revers_2 0.08055190000000001 sec
revers_3 0.17612719999999998 sec
my_revers_3 0.11475329999999995 sec

5 замер
revers_1 0.09129330000000002 sec
revers_2 0.08560769999999998 sec
revers_3 0.10015550000000001 sec
my_revers_3 0.0931052 sec

По замерам сложно определить, какая функция эффективнее.
Разница во времени исполнения лежит в пределах погрешности.


"""

