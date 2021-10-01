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
    n_list = list(str(enter_num))
    n_list.reverse()
    rest_num = ''.join(n_list)
    return rest_num


n = 1234567890
print(revers_1(n))
print(revers_2(n))
print(revers_3(n))
print(revers_4(n))

print(f'Реурсия:', timeit("revers_1(n)", globals=globals()))
print(f'Цикл:', timeit("revers_2(n)", globals=globals()))
print(f'Срез:', timeit("revers_3(n)", globals=globals()))
print(f'Ревесрс:', timeit("revers_4(n)",  globals=globals()))
run('revers_1(n)')
run('revers_2(n)')
run('revers_3(n)')
run('revers_4(n)')


"""
Реурсия: 5.325731063
Цикл: 3.811784458
Срез: 0.688182157
Ревесрс: 1.2395726269999994


Рекурсия самая медленная имеет сложность О(х^n)
Самый быстрый вариант через срез сложнонось которого O(k)(где k-количество элементов в срезе)
в отличии от цикла O(n) и реверса O(n).
Данные замеры нам показывают, что реверс и цикл имея равную сложность выполняются разное время.
"""