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
    """Реверс - 1 вариант"""
    enter_list = list(str(enter_num))
    enter_list.reverse()
    return ''.join(enter_list)


def revers_5(enter_num):
    """Реверс - 2 вариант"""
    return ''.join(reversed(str(enter_num)))


if __name__ == '__main__':
    numb = 123456789 ** 10
    print(f'************ "timeit" ************')
    print(f'1) revers_1 > '
          f'{timeit("revers_1(numb)", number=10000, globals=globals())}')
    print(f'2) revers_2 > '
          f'{timeit("revers_2(numb)", number=10000, globals=globals())}')
    print(f'3) revers_3 > '
          f'{timeit("revers_3(numb)", number=10000, globals=globals())}')
    print(f'3) revers_4 > '
          f'{timeit("revers_4(numb)", number=10000, globals=globals())}')
    print(f'3) revers_5 > '
          f'{timeit("revers_5(numb)", number=10000, globals=globals())}')
    print('\n')

    print(f'********** cProfile ***********')
    run('revers_1(numb)')
    run('revers_2(numb)')
    run('revers_3(numb)')
    run('revers_4(numb)')
    run('revers_5(numb)')

"""
Рекурсивная функция "revers_1" - самая медленная. Профилировка через cProfile показалала 85 вызовов.
Реализация через цикл в "revers_2" немного быстрее.
Способ через срез "revers_3" самый эффективный, т.к. без арифметики в цикле и рекурсии.
Варианты "revers_4" и "revers_5" немного более эффективны цикла, но менее эффективны среза; из-за преобразований встроенных функций.
"""
