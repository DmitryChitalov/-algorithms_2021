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
number = 123456789


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
    """Функция переворачивающая число с помощью функции reversed"""
    enter_num_str = str(enter_num)
    res = int(''.join(reversed(enter_num_str)))
    return res


print('TIMEIT')
print(f'Рекурсия:{timeit("revers_1(number)", globals=globals(), number=1000)}')
print(f'Цикл while:{timeit("revers_2(number)", globals=globals(), number=1000)}')
print(f'Списковые индексы:{timeit("revers_3(number)", globals=globals(), number=1000)}')
print(f'Функция reversed:{timeit("revers_4(number)", globals=globals(), number=1000)}')
print('cProfile')
print(f'Рекурсия:{run("revers_1(number)")}')
print(f'Цикл while:{run("revers_2(number)")}')
print(f'Списковые индексы:{run("revers_3(number)")}')
print(f'Функция reversed:{run("revers_4(number)")}')


"""
Ниже выведены результаты замеров. 
Замеры сделанные с помощью timeit показывают, что наиболее быстрым
является вариант с использованием списковых индексов. Близкий с ним результат
показал мой вариант со встроенной функцией reversed. Обе функции имеют линейную
сложность. Чуть меньший показатель скорости у reversed наверное объясняется тем,
что она возвращает объект класса reversed и к нему нужно применять join и int.
Вариант с рекурсией имеет сложность (9n)- столько раз вызывается функция. Это 
самый медленный вариант. Также к медленным можно отнести цикл while, т.к. он также 
многократно проходится пообъекту.
Вариант замеров с помощью cProfile показал все 0000, т.к. он делает всего
один прогон + делит функциюна операции (соответственно делится и общее время,
+ имеет ограничение 3  цифры после запятой, что не удобно при замерах скорости
работы кода с небольшими входящими данными.

TIMEIT
Рекурсия:0.0022429999999999985
Цикл while:0.001383299999999997
Списковые индексы:0.0003813000000000011
Функция reversed:0.0007150000000000004
cProfile
         13 function calls (4 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     10/1    0.000    0.000    0.000    0.000 task_3.py:21(revers_1)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Рекурсия:None
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:31(revers_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Цикл while:None
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:39(revers_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Списковые индексы:None
         5 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:45(revers_4)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}


Функция reversed:None
"""

