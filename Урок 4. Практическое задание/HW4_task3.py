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

# рекурсивная функция
def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)

# цикл
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num

# срез
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

# использование reverse списка
def revers_4(enter_num):
    new_list = list(enter_num)
    new_list.reverse()
    reversed_string = "".join(n_list)
    return reversed_string

enter_num = int(input('Введите целое число: '))
revers_1(enter_num, revers_num=0)
revers_2(enter_num, revers_num=0)
revers_3(enter_num)
revers_4(enter_num)



print(
    'рекурсия число наоборот: ',
    timeit(
        f'revers_1({enter_num})',
        globals=globals(),
        number=10000))
print(
    'цикл число наоборот: ',
    timeit(
        f'revers_2({enter_num})',
        globals=globals(),
        number=10000))
print(
    'срез число наоборот: ',
    timeit(
        f'revers_3({enter_num})',
        globals=globals(),
        number=10000))

print(
    'list reverse число наоборот: ',
    timeit(
        f'revers_4({enter_num})',
        globals=globals(),
        number=10000))


cProfile.run('revers_1(10000000000)')
cProfile.run('revers_2(10000000000)')
cProfile.run('revers_3(10000000000)')
cProfile.run('revers_4(10000000000)')


"""
Результат

Введите целое число: 123487681723648713264
рекурсия число наоборот:  0.0562125
цикл число наоборот:  0.033897899999999925
срез число наоборот:  0.003546500000000119
list reverse число наоборот:  0.007915699999999859
         15 function calls (4 primitive calls) in 0.026 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     12/1    0.000    0.000    0.000    0.000 main.py:21(revers_1)
        1    0.026    0.026    0.026    0.026 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 main.py:31(revers_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 main.py:39(revers_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         6 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 main.py:45(revers_4)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'reverse' of 'list' objects}



Process finished with exit code 0

С количеством выполняемых функций 100000:

Введите целое число: 551234651237471234765
[5.674321747321565e+20, 5.674321747321565e+20, '567432174732156432155', '567432174732156432155']
рекурсия число наоборот:  0.5373900000000003
цикл число наоборот:  0.339048
срез число наоборот:  0.03649140000000006
list reverse число наоборот:  0.08202630000000077


по замеру времени и по профилированию рекурсия - самый медленный и наименее эффективный способ решения (количество вызовов функции 12 и время выполнения больше, чем у других)
наиболее быстрый способ - срез, также list reverse работает быстре, чем цикл и рекурсия, хоть и медленнее, чем срез


