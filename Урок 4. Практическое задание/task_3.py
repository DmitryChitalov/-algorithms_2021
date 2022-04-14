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


def revers_4(enter_num):
    if enter_num == 0:
        return ''
    return f'{str(enter_num % 10)}{revers_4(enter_num // 10)}'


my_num = 12345


def my_all():
    return revers_1(my_num), revers_2(my_num), revers_3(my_num), revers_4(my_num)


run('my_all()')

print(timeit('revers_1(my_num)', globals=globals(), number=1000))  # 0.0022506979999999954    - 3
print(timeit('revers_2(my_num)', globals=globals(), number=1000))  # 0.0014989080000000071    - 2
print(timeit('revers_3(my_num)', globals=globals(), number=1000))  # 0.0007237110000000019    - 1
print(timeit('revers_4(my_num)', globals=globals(), number=1000))  # 0.0037509170000000064    - 4


'''Вывод: судя по профилерофки можно судить о том что, самой быстрой оказалась функция revers_3. Функции 
revers_1, revers_4 медлинее посколку там имеется рекурся, о наличии ее нам показует модуль cProfile. Функция revers_2
использует цикл и на каждом цикле производит вычисление, а также переопределяет переменные. Big(O) функции revers_2 
посчитать затруднительно но по профилировке видно что она медлинее чем revers_3. Ну а функция revers_3 берет число и
 разворачивает его по индексам, и это получается сделать быстрее, даже если число будет длинным.'''