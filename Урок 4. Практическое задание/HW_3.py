from cProfile import run
from timeit import timeit

my_num = 235286


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
    enter_num = str(enter_num)
    for el in enter_num:
        revers_num = enter_num[::-1]
    return revers_num


print(timeit(
    f'revers_1({my_num})',
    globals=globals(),
    number=10000))
print(timeit(
    f'revers_2({my_num})',
    globals=globals(),
    number=10000))
print(timeit(
    f'revers_3({my_num})',
    globals=globals(),
    number=10000))
print(timeit(
    f'revers_4({my_num})',
    globals=globals(),
    number=10000))

run('revers_1(my_num)')
run('revers_2(my_num)')
run('revers_3(my_num)')
run('revers_4(my_num)')

"""
ИТОГ: судя по полученным данным наиболее быстрой является 3 функция
Получение среза строки логично быстрее чем любые операции с вычеслениями.
А в рекурсии тем более.
"""
