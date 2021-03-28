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


number = 192837465192837465987654321

result = dict()

for i in ['revers_1(number)', 'revers_2(number)', 'revers_3(number)']:
    t = timeit(i, globals=globals(), number=10000)
    result[i] = t

print(f"Самая быстрая функция ---> {sorted([(v,k) for k, v in result.items()])[0][1]}")

for i in ['revers_1(number)', 'revers_2(number)', 'revers_3(number)']:
    run(i)

'''
По результатам выполнения профайлеров видим что самая быстрая это функция revers_3.
revers_1 медленная из за того что она рекурсивная
revers_2 на втором месте, быстрее revers_1 потому что используется итеративный подход
revers_3 самая быстрая потому что использует слайс, а он втроеный в python и соответственно оптимизирован под быстрое
выполнение
'''