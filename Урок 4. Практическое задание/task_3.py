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
from random import randint

"""
Первая функция рекурсивная, имеет сложность О(n^2), поэтому самая медленная из всех
"""


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


"""
Вторая - имеет сложность O(n), быстрее первой, но медленнее третьей
"""


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


"""
Третья имеет также имеет линейную сложность, однако здесь нет цикла
с таким количеством операций, как во второй функции, здесь используется 
реверс строки с использованием среза
"""


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


"""
Можно использовать встроенные функции join и reversed, однако поскольку
одна вложена в другую, функция будет выполняться дольше, чем третья
"""


def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


number = randint(100000, 1000000)
print(f'Число: {number}')

print(timeit('revers_1(number)', globals=globals()))
print(timeit('revers_2(number)', globals=globals()))
print(timeit('revers_3(number)', globals=globals()))
print(timeit('revers_4(number)', globals=globals()))


def main():
    revers_1(number)
    revers_2(number)
    revers_3(number)
    revers_4(number)


run('main()')
