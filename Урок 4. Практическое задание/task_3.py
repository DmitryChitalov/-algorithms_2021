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
import timeit
import cProfile


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


def revers_my(enter_num, revers_num=0):
    for _ in range(len(str(enter_num))):
        revers_num = (revers_num + (enter_num % 10) / 10) * 10
        enter_num //= 10
    return revers_num


print('revers_1', timeit.timeit('revers_1(5246)', 'from __main__ import revers_1', number=100000))
print('revers_1', timeit.repeat('revers_1(5246)', globals=globals(), repeat=5, number=100000))
cProfile.run('revers_1(5246)')
print()

print('revers_2', timeit.repeat('revers_2(5246)', globals=globals(), repeat=7, number=(10 ** 5)))
cProfile.run('revers_2(5246)')
print()

print('revers_3', timeit.repeat('revers_3(5246)', globals=globals(), number=(10**5)))
cProfile.run('revers_3(5426)')


print('revers_my', timeit.repeat('revers_my(5246)', globals=globals(), number=(10**5)))
cProfile.run('revers_my(5426)')
print(revers_my(5246))


""" Входе исптаний я установил следующее. Самы эффективный - быстрый является реализация
revers_3 за ней revers_2, revers_1 = revers_my. Для меня было удивительно что revers_2 faster
revers_my потому что цикл for faster while, я предполагаю, это из за реализации
цикла for потребовалось больше сторонних операций range(len(str(enter_num)), профилировка 
это подверждает в for  на 1 вызов бльше
"""