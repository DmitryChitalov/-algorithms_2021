"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящего в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективное и почему !!!
Без аналитики задание считается не принятым
"""
import cProfile
from timeit import timeit


# Рекурсия
def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


# Цикл While
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


# Цикл for
def revers_4(enter_num):
    decision = ''
    for bulkhead in str(enter_num):
        decision = bulkhead + decision
    return decision


user_number = int(input('Введите число: '))

print(revers_1(user_number))
print(revers_2(user_number))
print(revers_3(user_number))
print(revers_4(user_number))
print('_' * 500)

print(timeit("revers_1(user_number)", globals=globals()))  # 2.3500230999999996 - рекурсия
print(timeit("revers_2(user_number)", globals=globals()))  # 1.5192562          - цикл while
print(timeit("revers_3(user_number)", globals=globals()))  # 0.3626756999999996 - срез
print(timeit("revers_4(user_number)", globals=globals()))  # 0.9556000000000004 - цикл for
print('_' * 500)

cProfile.run("revers_1(user_number)")
print('_' * 500)
cProfile.run("revers_2(user_number)")
print('_' * 500)
cProfile.run("revers_3(user_number)")
print('_' * 500)
cProfile.run("revers_4(user_number)")

"""
 13 function calls (4 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     10/1    0.000    0.000    0.000    0.000 3.py:18(revers_1)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 3.py:28(revers_2)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 3.py:36(revers_3)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 3.py:42(revers_4)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

"""
    Вывод: Исходя из замеров выполнения функций формирующих из введенного числа
обратное по порядку входящего в него число, можно сделать вывод что самой быстрой по выполнению функцией

будет Срез, т.к. просто переворачивает число практический не затрачивая на это ресурсы.

На втором месте по скорости выполнения будет цикл for, т.к. перебирает каждое входящее в него число и записывает 
в обратном порядке затрачивая на это немногожко больше ресурсов чем срез, но не так много.

На третьем месте по скорости выполнения будет цикл while, т.к. выполнение происходит через условие, 
и цикл не завершится пока количество входящих элементов не будет равное 0, при этом проходя через определенные
вычесления и затрачивая уже больше ресурсов для перебора.

И на последнем месте по скорости выполнения будет рекурсия, т.к. выполнение происходит методом вызова самой себя
и использует стек при переборке входящих элементов 
"""
