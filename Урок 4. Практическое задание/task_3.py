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


def revers_4(enter_num):
    """Реверс вариант 1"""
    enter_list = list(str(enter_num))
    enter_list.reverse()
    return ''.join(enter_list)


def revers_5(enter_num):
    """Реверс вариант 2"""
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
Самая медленная функция это - "revers_1" так как она рекурсивная, профилировка чрез cProfile
показала 85 вызовов этой фун.
Чуть быстрее реализация через цикл "revers_2"
И самый эффективный способ через срез "revers_3" он самый простой, так как без арифметических вычислений как в цикле 
и рекурсии.

Два вариант что я написал (revers_4, revers_5), чуть эффективнее цикла, но хуже среза, в связи 
с наличием преобразований и встроенных функций

"""