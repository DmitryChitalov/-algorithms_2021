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


# не стал писать отдельный декоратор для замера времени с помощью cProfile, чтобы правиьно замерить время выполнения
# функций reverse_1, reverse_2, reverse_3
def reverse_1_cProfile():
    enter_num = 12345678912345678912345678912345678912345678900000000000000000000065463234253256572123415225353643
    for i in range(10000):
        revers_1(enter_num)


def reverse_2_cProfile():
    enter_num = 12345678912345678912345678912345678912345678900000000000000000000065463234253256572123415225353643
    for i in range(10000):
        revers_2(enter_num)


def reverse_3_cProfile():
    enter_num = 12345678912345678912345678912345678912345678900000000000000000000065463234253256572123415225353643
    for i in range(10000):
        revers_3(enter_num)


# собственный вариант решения, похожий на функцию revers_2
def own_reverse_number(enter_number):

    new_number = 0
    while enter_number > 0:
        digit = enter_number % 10
        enter_number //= 10
        new_number *= 10
        new_number += digit

    return new_number


def own_reverse_number_cProfile():
    enter_number = 12345678912345678912345678912345678912345678900000000000000000000065463234253256572123415225353643
    for i in range(10000):
        own_reverse_number(enter_number)


number = 12345678912345678912345678912345678912345678900000000000000000000065463234253256572123415225353643

# revers_1 - рекурсивная функция, также в реализации присутствует много операций вычисления и присваивания =>
# наиболее долгое время выполнения
# revers_2 - итеративное решение, которое по времени выполнения выигрывает перед рекурсивной реализацией
# revers_3 - в решении используется встроенная функция str(), а также срез в обратном порядке всего массива, полностью
# отстутвуют вычислительные операции => данная функция будет отрабатывать быстрее, чем reverse_2
print(timeit.timeit('revers_1(number)', number=10000, globals=globals()))  # результат: 0.81 с
print(timeit.timeit('revers_2(number)', number=10000, globals=globals()))  # результат 0.48 с
print(timeit.timeit('revers_3(number)', number=10000, globals=globals()))  # результат 0.021 с

# в выводе получаем, что все значения в столбце cumtime для каждой из функций revers_1, revers_2 и revers_3 несколько
# отличаются от значений, полученных с помощью timeit
run('reverse_1_cProfile()') # результат 1.046 с
run('reverse_2_cProfile()') # результат 0.479 с
run('reverse_3_cProfile()') # результат 0.017 с

# для собственной функции результат выполнения 0.483 с => оптимизация не удалась, результат близкий к reverse_2
print(timeit.timeit('own_reverse_number(number)', number=10000, globals=globals()))

# cumtime = 0.568
run('own_reverse_number_cProfile()')