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


def revers_4(enter_num, revers_num=''):
    enter_num = str(enter_num)
    for i in range(len(enter_num)):
        revers_num = revers_num + enter_num[(len(enter_num) - 1) - i]
    return revers_num


enter_num = int(input("Number: "))

revers_1(enter_num, revers_num=0)
revers_2(enter_num, revers_num=0)
revers_3(enter_num)
revers_4(enter_num, revers_num='')


print(
    timeit.timeit(
        f'revers_1({enter_num})',
        globals=globals(),
        number=1000)
)

print(
    timeit.timeit(
        f'revers_2({enter_num})',
        globals=globals(),
        number=1000)
)


print(
    timeit.timeit(
        f'revers_3({enter_num})',
        globals=globals(),
        number=1000)
)

print(
    timeit.timeit(
        f'revers_4({enter_num})',
        globals=globals(),
        number=1000)
)


# enter_num = 5987
# revers_1 0.0014438999999999425   O(2**n) Самый медленнаый это рекурсивной способ O(2**n)
# revers_2 0.0009062000000001902   O(n)
# revers_3 0.0003251999999998034   O(b - a)
# revers_4 .00113709999999978      O(n)
# вывод: реализация через срез является самой эффективной т.к. строка в pythom является итерационным типом ,
# следовательно мы можем легко обработать каждый отдельный символ в строке как часть последовательного расположения элементов.

