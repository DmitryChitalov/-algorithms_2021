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
import cProfile


# Рекурсия
def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


# Цикл
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


enter_num = int(input('Введите целое число: '))

revers_1(enter_num, revers_num=0)
revers_2(enter_num, revers_num=0)
revers_3(enter_num)


print(
    'Число наоборот на рекурсиях: ',
    timeit(
        f'revers_1({enter_num})',
        globals=globals(),
        number=10000))
print(
    'Число наоборот на циклах: ',
    timeit(
        f'revers_2({enter_num})',
        globals=globals(),
        number=10000))
print(
    'Число наоборот на срезах: ',
    timeit(
        f'revers_3({enter_num})',
        globals=globals(),
        number=10000))

cProfile.run('revers_1(10000000000)')
cProfile.run('revers_2(10000000000)')
cProfile.run('revers_3(10000000000)')



# Рекурсия и цикл медленее среза из-за количества вычислений, производимых внутри функции.
