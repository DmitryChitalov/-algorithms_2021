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


# мой вариант решения через список и метод reverse()
def my_reverse(number):
    number = str(number)
    list_obj = list(number)
    list_obj.reverse()
    reverse_num = ''.join(list_obj)
    return reverse_num


if __name__ == '__main__':
    number = 345642323233345562
    # профилирование функции revers_1:
    print(f'Профилирование функции revers_1 спомощью timeit: время выполнения функции - {timeit("revers_1(number)", globals=globals())}')
    print(f'Провилирование функций revers_1, revers_2 и revers_3  спомощью cProfile:\n')
    run('revers_1(number)')
    print('================================================================================================')
    print()
    # профилирование функции revers_2:
    print(f'Профилирование функции revers_2 спомощью timeit: время выполнения функции - {timeit("revers_2(number)", globals=globals())}')
    print(f'Провилирование функции revers_2 спомощью cProfile:\n')
    run('revers_2(number)')
    print('================================================================================================')
    print()
    # профилирование функции revers_3:
    print(f'Профилирование функции revers_3 спомощью timeit: время выполнения функции - {timeit("revers_3(number)", globals=globals())}')
    print(f'Провилирование функции revers_3 спомощью cProfile:\n')
    run('revers_3(number)')
    print('================================================================================================')
    print()

    # профилирование моего решения через список и метод reverse() - функция my_reverse:
    print(f'Профилирование функции my_reverse спомощью timeit: время выполнения функции - {timeit("my_reverse(number)", globals=globals())}')
    print(f'Провилирование функции my_reverse спомощью cProfile:\n')
    run('my_reverse(number)')

"""
Выводы:
Наиболее эффективная реализация через срез (revers_3).
Время ее исполнения существенно ниже в сравнении с рекурсией и циклом,
потому что нет операций взятия остатка и целочисленного деления и др.
"""

