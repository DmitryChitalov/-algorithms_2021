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
import cProfile
import timeit

# Рекурсия
def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)

# цикл while
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num

# срез
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

# reversed + join
def revers_4(enter_num):
    revers_num = ''.join(reversed(str(enter_num)))
    return revers_num

NUMS = 123456789
print(revers_1(NUMS))
print(revers_2(NUMS))
print(revers_3(NUMS))
print(revers_4(NUMS))

print(
    timeit.timeit(
        "revers_1(NUMS)",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "revers_2(NUMS)",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "revers_3(NUMS)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "revers_4(NUMS)",
        globals=globals(),
        number=1000))

cProfile.run('revers_1(1000000)')
cProfile.run('revers_2(1000000)')
cProfile.run('revers_3(1000000)')
cProfile.run('revers_4(1000000)')

"""
reversed + join дают неплохой результат, но срез лучше
"""