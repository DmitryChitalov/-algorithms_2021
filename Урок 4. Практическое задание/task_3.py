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
from timeit import timeit

import random

"""
Создадим функцию для замера времени
"""


def get_time(funk_str):
    print(timeit(funk_str, number=10000, globals=globals()))


# Исходные функции реверса
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


# Предлагаю функцию реверса
def my_reverse_2(enter_num):
    string_lst = list(str(enter_num))
    string_lst.reverse()
    return ''.join(string_lst)


# Генерируем и выводим число
enter_num = random.randrange(1000000, 100000000000)
print(f"Исходное число: {enter_num}")

# Создаем словарь для обхода созданных функций в timeit и вывода их значений
func_dict = {'revers_1(enter_num, revers_num=0)': revers_1(enter_num, revers_num=0),
            'revers_2(enter_num, revers_num=0)': revers_2(enter_num, revers_num=0),
            'revers_3(enter_num)': revers_3(enter_num),
            'my_reverse_2(enter_num)': my_reverse_2(enter_num)}


for key,  el in func_dict.items():
    print(f'Наименование и параметры функции: {key}. Результирующее значение: {el}')
    print('Данные замера времени timeit:', end=' ')
    get_time(key)
    # Для каждой функции исполняем код
    cProfile.run(
        f'{key},'*10000
    )


"""
Исходное число: 149479899
Наименование и параметры функции: revers_1(enter_num, revers_num=0). Результирующее значение: 998974941.0
Данные замера времени timeit: 0.0453124
Наименование и параметры функции: revers_2(enter_num, revers_num=0). Результирующее значение: 998974941.0
Данные замера времени timeit: 0.020624699999999996
Наименование и параметры функции: revers_3(enter_num). Результирующее значение: 998974941
Данные замера времени timeit: 0.004499799999999998
Наименование и параметры функции: my_reverse_2(enter_num). Результирующее значение: 998974941
Данные замера времени timeit: 0.0078067000000000275

По данным замера времени timeit наиболее предпочтительна реализация: revers_3(). 
Реализация my_reverse_2() получилась неплохая, но медленнее на 0,003

По данным исполнения каждой функции 10000 раз cProfile статистика в cumtime показывает более существенный, 
но сопоставимый разброс между фкнкциями:
revers_1 - 0.074
revers_2 - 0.029
revers_3 - 0.006
my_reverse_2 - 0.015

Вывод подтвержден: revers_3 лучший вариант (в первую очередь, в силу низкой сложности).
"""

# Вызов cProfile для получения сопоставимых результатов с timeit

cProfile.run('revers_1(enter_num, revers_num=0), revers_2(enter_num, revers_num=0),'
             'revers_3(enter_num), my_reverse_2(enter_num), ' * 10000)

"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.015    0.015    0.140    0.140 <string>:1(<module>)
120000/10000    0.074    0.000    0.074    0.000 task_3.py:31(revers_1)
    10000    0.029    0.000    0.029    0.000 task_3.py:41(revers_2)
    10000    0.006    0.000    0.006    0.000 task_3.py:49(revers_3)
    10000    0.011    0.000    0.015    0.000 task_3.py:56(my_reverse_2)
        1    0.374    0.374    0.513    0.513 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    10000    0.003    0.000    0.003    0.000 {method 'join' of 'str' objects}
    10000    0.001    0.000    0.001    0.000 {method 'reverse' of 'list' objects}
"""