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


def revers_4(enter_num):
    l = list(str(enter_num))
    l.reverse()
    return ''.join(l)

n = int(input())

revers_1(n, revers_num=0)
revers_2(n, revers_num=0)
revers_3(n)
revers_4(n)


""" Проводим замеры """
t1 = timeit("revers_1(n)", globals=globals(),number=1000)
t2 = timeit("revers_2(n)", globals=globals(),number=1000)
t3 = timeit("revers_3(n)", globals=globals(),number=1000)
t4 = timeit("revers_4(n)", globals=globals(),number=1000)
print(t1)
print(t2)
print(t3)
print(t4)
""" Результаты замеров через timeit
0.0016948999999999437
0.0011415000000001285
0.0005664999999996922
0.0009019999999999584"""


cProfile.run('revers_1(10000000000)')
cProfile.run('revers_2(10000000000)')
cProfile.run('revers_3(10000000000)')

"""
Самым быстрым будет способ через срез (То есть это функция revers_3()), так как в ней нет арифметических действий, как есть в
функции revers_1()) и функции revers_2()), и нет рекурсии.
Мой вариант тоже довольно - таки неплохой. Он быстрее цикла, но медленнее среза из-за встренных функций
"""