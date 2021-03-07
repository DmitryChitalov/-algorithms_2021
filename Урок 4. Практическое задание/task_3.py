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
import cProfile
import timeit


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


numb = 123456789

print("Профилирование с помощью модуля timeit:\n")
print(f"""Функция: revers_1
Получено значение: {revers_1(numb)}
Затраченное время: {timeit.repeat('revers_1(numb)', 'from __main__ import revers_1, numb', repeat=3, number=1000000)}
""")
print(f"""Функция: revers_2
Получено значение: {revers_2(numb)}
Затраченное время: {timeit.repeat('revers_2(numb)', 'from __main__ import revers_2, numb', repeat=3, number=1000000)}
""")
print(f"""Функция: revers_3
Получено значение: {revers_3(numb)}
Затраченное время: {timeit.repeat('revers_3(numb)', 'from __main__ import revers_3, numb', repeat=3, number=1000000)}
""")

print("Профилирование с помощью модуля cProfile:\n")
print(f"""Функция: revers_1
Получено значение: {revers_1(numb)}
Результат профилирования:
""")
cProfile.run('revers_1(numb)')

print(f"""Функция: revers_2
Получено значение: {revers_2(numb)}
Результат профилирования:
""")
cProfile.run('revers_2(numb)')

print(f"""Функция: revers_3
Получено значение: {revers_3(numb)}
Результат профилирования:
""")
cProfile.run('revers_3(numb)')

'''
По результатам анализа было выявлено, что самое медленное исполнение у ф-ии revers_1,
т.к. оно исполняется рекурсивно. Самое быстрое исполнение - revers_3, т.к. используются
срезы, что практически схоже с обращением по индексу. На 2 месте revers_2, т.к. исп-ие
циклов исполняется, чем обращение по индексу, но быстрее чем рекурсия. 
'''
