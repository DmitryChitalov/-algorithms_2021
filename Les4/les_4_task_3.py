import timeit
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
    enter_num = list(str(enter_num))
    enter_num.reverse()
    return enter_num


def main():
    revers_1(123)
    revers_2(123)
    revers_3(123)
    revers_4(123)


run("main()")
print(f"Анализ функции 1 через timeit: {timeit.timeit('revers_1(123)', setup='from __main__ import revers_1', number=10000)}")
print(f"Анализ функции 2 через timeit: {timeit.timeit('revers_2(123)', setup='from __main__ import revers_2', number=10000)}")
print(f"Анализ функции 3 через timeit: {timeit.timeit('revers_3(123)', setup='from __main__ import revers_3', number=10000)}")
print(f"Анализ функции 4 через timeit: {timeit.timeit('revers_4(123)', setup='from __main__ import revers_4', number=10000)}")

"""Функция 3 быстрее, так как у неё меньше сложность"""
