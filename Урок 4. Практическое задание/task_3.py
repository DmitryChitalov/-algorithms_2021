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
from timeit import timeit, default_timer, repeat
from cProfile import run

NUM = 1234561234234
CNT = 100000


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
    s = [*str(enter_num)]       # вот здесь теряется 80% времени по отчету cPrifile
    new_str = ''
    while len(s):
        new_str += s.pop()
    return new_str

def many(cnt):
    def decor(func):
        def wrapper():
            for i in range(cnt):
                func()
        return wrapper
    return decor

@many(CNT)
def main():
    revers_1(NUM)
    revers_2(NUM)
    revers_3(NUM)
    revers_4(NUM)


run(statement='main()')

statements = ['revers_1(NUM)', 'revers_2(NUM)', 'revers_3(NUM)', 'revers_4(NUM)']

for st in statements:
    print(st, min(repeat(stmt=st,
                         globals=globals(),
                         timer=default_timer,
                         repeat=3,
                         number=CNT)))

'''
         4500004 function calls (3200004 primitive calls) in 5.797 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    5.797    5.797 <string>:1(<module>)
1400000/100000    1.979    0.000    1.979    0.000 task_3.py:23(revers_1)
   100000    0.788    0.000    0.788    0.000 task_3.py:33(revers_2)
   100000    0.280    0.000    0.280    0.000 task_3.py:41(revers_3)
   100000    1.503    0.000    2.229    0.000 task_3.py:47(revers_4)
        1    0.095    0.095    5.797    5.797 task_3.py:56(wrapper)
   100000    0.425    0.000    5.702    0.000 task_3.py:62(main)
        1    0.000    0.000    5.797    5.797 {built-in method builtins.exec}
  1400000    0.364    0.000    0.364    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1300000    0.362    0.000    0.362    0.000 {method 'pop' of 'list' objects}


revers_1(NUM) 0.9885026119882241
revers_2(NUM) 0.655579062004108
revers_3(NUM) 0.10466451200773008
revers_4(NUM) 0.6257348869985435

ВЫВОДЫ: 
1. лучший результат дают срезы и операции, которые максимально используют .
2. худший при (на порядок) рекурсия из-за О-сложности
3. сProfile весьма информативен, показывает, как отработало приложение, количество
вызовов функций и в целом беру эти два метода на вооружение))))
4. непонятно как объяснить данные по алгоритму 4. на сПрофайл у него худший результат по времени. 
При оценке timeit результат лучший. ))))))) просьба пояснить с чего такое может получаться?

'''
