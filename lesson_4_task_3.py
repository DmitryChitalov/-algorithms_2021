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


def revers_1(enter_num, revers_num=0):  # O(2^n)
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):  # O(n)
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):  # O(n)
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def my_reverse(n, help_number, reversed_number=0):  # O(2^n)
    reversed_number += str(help_number)
    if n // 10 == 0:
        reversed_number += str(n)  # конкатенация с последней цифрой
        return reversed_number
        quit()
    else:
        help_number = n % 10  # вспомогательная переменная, для получения отдельных цифр числа
    return my_reverse(n // 10, help_number, reversed_number)


print('cProfile')
print('-' * 50, 'revers_1', '-' * 50)
print(run('revers_1'))
print('-' * 50, 'revers_2', '-' * 50)
print(run('revers_2'))
print('-' * 50, 'revers_3', '-' * 50)
print(run('revers_3'))
print('-' * 50, 'my_reverse', '-' * 50)
print(run('my_reverse'))
print('-' * 50)
print('timeit:')
print(f'revers_1 {timeit("revers_1", globals=globals())}')
print(f'revers_2 {timeit("revers_2", globals=globals())}')
print(f'revers_3 {timeit("revers_3", globals=globals())}')
print(f'my_reverse {timeit("my_reverse", globals=globals())}')
'''
timeit:
revers_1 0.06002039999999999
revers_2 0.056673399999999985
revers_3 0.05594099999999999
my_reverse 0.06409140000000002

'''
'''
Из 4-х способов решения задачи самым быстрым является срез (вариант 3).
Несмотря на то, что у него такая же сложность, как у цикла (вариант 2), в нём не выполняются арифметические действия,
поэтому он быстрее 
'''